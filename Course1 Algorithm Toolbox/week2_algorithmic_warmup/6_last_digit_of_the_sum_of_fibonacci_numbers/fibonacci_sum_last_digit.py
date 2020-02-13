# Uses python3
import sys



def sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum

def sum_(n):
    if n <= 1:
        return n
    
    n = n%60
    return sum_naive(n)%10


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(sum_(n))
    