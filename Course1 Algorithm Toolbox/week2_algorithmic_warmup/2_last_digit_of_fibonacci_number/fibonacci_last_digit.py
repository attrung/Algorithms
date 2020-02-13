# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n
    prev = 1
    curr = 1
    for i in range(2,n):
        temp = curr
        curr = (prev + curr)%10
        prev = temp
    return curr

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
