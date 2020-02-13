#Uses python3
import sys
import math

def sort_point(x,y):
    index = sorted(range(len(x)),key=x.__getitem__)
    new_x = []
    new_y = []
    for i in index:
        new_x.append(x[i])
        new_y.append(y[i])
    return new_x, new_y

def sort_point_y(x,y):
    index = sorted(range(len(y)),key=y.__getitem__)
    new_x = []
    new_y = []
    for i in index:
        new_x.append(x[i])
        new_y.append(y[i])
    return new_x, new_y


def minimum_distance(x, y):
    if len(x) == 1:
        d = math.inf
        return d
    mid = len(x)//2
    d1 = minimum_distance(x[0:mid],y[0:mid])
    d2 = minimum_distance(x[mid:len(x)],y[mid:len(x)])
    d = min(d1,d2)
    l = x[mid] - d
    r = x[mid] + d
    li = 0
    ri = len(x)
    for i in range(len(x)-1):
        if x[i] < l < x[i+1]:
            li = i
        if x[i] < r < x[i+1]:
            ri = i
    new_x, new_y = sort_point_y(x[li:ri], y[li:ri])
    for i in range(len(new_x)):
        for j in range(1,8):
            if i + j >= len(new_x):
                break
            length = ((x[i+j] - x[i])**2 + (y[i+j] - y[i])**2)**(1/2)
            if length < d: 
                d = length
    return d

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    x, y = sort_point(x,y)
    print("{0:.4f}".format(minimum_distance(x,y)))
