# Uses python3
import sys

def find_length(m):
    mod_li = [0]
    i = 0
    while True:
        for j in range(2):
            mod_li.append(find_fib(i + j + 1)%m)
        i += 2
        if mod_li[0:int(i/2)] == mod_li[int(i/2):i]:
            return int(i/2)
            break

def long(n, m):
    if n <= 1:
        return n
    
    else: 
        length = find_length(m)
        if n > length:
            n = n%length
        return find_fib(n) % m

def find_fib(n):
    if n == 0:
        return 0
    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(long(n, m))