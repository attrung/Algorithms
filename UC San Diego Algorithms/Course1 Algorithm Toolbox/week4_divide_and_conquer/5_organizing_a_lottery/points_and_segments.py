# Uses python3
import sys

def binary_search(a, x, ans = 0):
    left, right = 0, len(a)
    mid  = int((left + right)/2)
    if right == left:
        return -1
    y1 = a[mid-1]
    y2 = a[mid]
    if x < y1:
        return binary_search(a[left:mid-1], x, ans)
    elif x > y2:
        ans += mid
        if mid < right-1:
            if x < a[mid + 1]:
                return ans + mid
        return binary_search(a[mid+1:right], x, ans)
    if y1< x <= y2:
        return ans + mid
    return -1

def fast_count_segments(starts, ends, points):
    cnt = []
    org = points.copy()
    points = sorted(points)
    count = {}
    for value in points:
        count[value] = 0
    for i in range(len(starts)):
        s = binary_search(points, starts[i])
        if s == -1:
            s = 0
        e = binary_search(points, ends[i])
        if e == -1:
            e = None
        if starts[i] < points[-1] and ends[i] > points[0]:
            for j in points[s:e]:
                count[j] += 1
    for value in org:
        cnt.append(count[value])
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
