# Uses python3
import sys

def get_change(m):
    least = [1,2,1,1]
    if m < 4:
        return least[m-1]
    for i in range(4, m):
        change1 = least[i-4] + 1
        change2 = least[i-3] + 1
        change3 = least[i-1] + 1
        least.append(min(change1, change2, change3))
    return least[-1]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
