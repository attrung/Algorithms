# Uses python3
import sys

def gcd(a, b):
    small = min([a,b])
    big= max([a,b])
    if big%small == 0:
        return small
    else:
        return gcd(small, big%small)
    
#    for d in range(2, min(a, b) + 1):
#        if a % d == 0 and b % d == 0:
#            if d > current_gcd:
#                current_gcd = d
#
#    return current_gcd

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
