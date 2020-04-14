# Uses python3
import sys

def gcd(a, b):
    small = min([a,b])
    big= max([a,b])
    if big%small == 0:
        return small
    else:
        return gcd(small, big%small)

def lcm(a, b):
    if a == 0 or b == 0:
        return 0    
    return int(a*b/(gcd(a,b)))

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

