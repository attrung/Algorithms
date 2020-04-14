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
    if n < 1:
        return 0
    elif n == 1:
        return 1
    
    n = n%60
    return sum_naive(n)%10

def fibonacci_partial_sum_naive(from_, to):
    
    return (sum_(to) - sum_(from_ - 1) + 10)%10
    
#    sum = 0
#
#    current = 0
#    next  = 1
#
#    for i in range(to + 1):
#        if i >= from_:
#            sum += current
#
#        current, next = next, current + next
#
#    return sum % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))