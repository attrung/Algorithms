# Uses python3
import sys

def get_change(m):
    possible = [10,5,1]
    n = 0
    for i in possible:
        n += m//i
        m = m%i
    return n

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
