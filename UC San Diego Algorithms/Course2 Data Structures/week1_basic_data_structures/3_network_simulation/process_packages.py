# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []
        self.current_buff = []
        
    def process(self, request):
        if request != 'dropped':
            new_finish_time = max(self.finish_time[-1] + request[1], request[0] + request[1])
            self.finish_time.append(new_finish_time)
            self.current_buff.pop(0)
            return Response(False, max(self.finish_time[-2], request[0]))
        else:
            return Response(True, -1)
        return Response(False, -1)



def process_requests(requests, buffer):
    responses = []
    for i in range(0, len(requests)):
        if i == 0:
            buffer.finish_time.append(max(requests[i][0], 0))
        if requests[i] != 'dropped':
            start = requests[i][0]
            buffer_time = buffer.finish_time[-1]
            start = max(start, buffer_time)
            end = start + requests[i][1]
            for j in range(i, len(requests)):
                if requests[j] != 'dropped':
                    if start <= requests[j][0] < end or requests[i][1] == 0:
                        if j not in buffer.current_buff:
                            buffer.current_buff.append(j)
                    elif requests[j][0] > end:
                        break
            if len(buffer.current_buff) > buffer.size and requests[i][1] != 0:
                elim = buffer.current_buff[buffer.size:]
                buffer.current_buff = buffer.current_buff[:buffer.size]
                for k in elim:
                    requests[k] = 'dropped'
            responses.append(buffer.process(requests[i]))
        else:
            responses.append(buffer.process(requests[i]))
    return responses

def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
    
    
#    for i in range(len(requests)):
#        if requests[i] != 'dropped':
#            start = requests[i][0]
#            end = requests[i][0] + requests[i][1]
#            cize = 0
#            for j in range(j + 1, len(requests)):
#                if requests[j][0]
