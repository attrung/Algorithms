# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    low = []
    high = []
    #write your code here
    for s in segments:
        low.append(s[0])
        high.append(s[1])
    index = sorted(range(len(high)),key = high.__getitem__)
    points = []
    while True:
        a = high[index[0]]
        points.append(a)
        i = 0
        while i < len(index):
            if low[index[i]] <= a <= high[index[i]]:
                index.pop(i)
            else:
                i += 1
        if index == []:
            break
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
