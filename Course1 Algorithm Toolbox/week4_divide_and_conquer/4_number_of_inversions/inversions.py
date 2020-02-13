# Uses python3
import sys

def join_array(a,b):
    count = 0
    x = 0
    y = 0
    a_len = len(a)
    b_len = len(b)
    output = []
    for i in range(a_len+b_len):
        if x == a_len:
            output += b[y:b_len]
            break
        if y == b_len:
            output += a[x:a_len]
            break
        if a[x]>b[y]:
            output.append(b[y])
            count += a_len-x
            y += 1
        else:
            output.append(a[x])
            x += 1
    return output, count

def main(data):
    if len(data) == 1:
        return 0, data
    n = len(data)
    x = n//2
    left = data[0:x]
    right = data[x:n]
    answer_left = main(left)
    answer_right = main(right)
    answer = join_array(answer_left[1], answer_right[1])
    return answer_left[0] + answer[1] + answer_right[0], answer[0]

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(main(a)[0])
