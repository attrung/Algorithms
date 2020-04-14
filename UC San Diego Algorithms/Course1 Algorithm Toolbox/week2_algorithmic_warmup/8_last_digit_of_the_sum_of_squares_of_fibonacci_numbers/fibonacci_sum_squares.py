# Uses python3
from sys import stdin

def long(n):
    if n <= 1:
        return n
    
    else: 
        length = 60
        if n > length:
            n = n%length
        return find_fib(n) % 10

def find_fib(n):
    if n == 0:
        return 0
    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current

def fibonacci_sum_squares(n):
    if n <= 1:
        return n
    
    else:
        return long(n)*long(n+1)%10
    

#    previous = 0
#    current  = 1
#    sum      = 1
#
#    for _ in range(n - 1):
#        previous, current = current, previous + current
#        sum += current * current

#    return sum % 10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares(n))
