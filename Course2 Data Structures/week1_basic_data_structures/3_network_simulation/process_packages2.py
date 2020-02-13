# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = [0]
        self.current_buff = []

    def process(self, request):
        time = max(request[0], self.finish_time[-1])
        self.finish_time.append(time + request[1])
        self.current_buff.pop(0)
        return Response(False, time)


def process_requests(requests, buffer):
    responses = [None]*len(requests)
    i = 0
    if len(requests) == 0:
        return []
    while True:
        if len(requests) == 1:
            buffer.current_buff.append([requests[i], i])
            i += 1
        else: 
            if i < len(requests):
                while len(buffer.current_buff) < buffer.size:
                    buffer.current_buff.append([requests[i], i])
                    i += 1
        m = buffer.current_buff[0][1]
        responses[m] = buffer.process(buffer.current_buff[0][0])
        for k in range(i, len(requests)):
            if requests[k][0] < buffer.finish_time[-1]:
                responses[k] = Response(True, -1)
                i = k + 1
            else:
                break
        if i >= len(requests) and len(buffer.current_buff) == 0:
            break
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
