# Uses python3
import sys

def binary_search(a, x, ans = 0):
    left, right = 0, len(a)
    mid  = (left + right)//2
    if right == left:
        return -1
    y = a[mid]
    if y == x:
        return ans + mid
    elif x < y: 
        return binary_search(a[left:mid], x, ans)
    elif x > y:
        ans += mid + 1
        return binary_search(a[mid+1:right], x, ans)
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
