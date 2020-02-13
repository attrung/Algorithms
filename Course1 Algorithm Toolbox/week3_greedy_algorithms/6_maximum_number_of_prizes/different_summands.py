# Uses python3
import sys

def optimal_summands(n):
    summands = []
    i = 1
    sum1 = 0
    while True:
        if sum1 + i + i + 1 <= n:
            sum1 += i
            summands.append(i)
            i += 1
        else:
            summands.append(n - sum1)
            break
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
