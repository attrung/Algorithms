#Uses python3

import sys

def lcs3(a, b, c):
    graph = {}
    for i in range(len(a)+1):
        for j in range(len(b)+1):
            for m in range(len(c)+1):
                if i == 0 or j == 0 or m == 0:
                    graph[(i,j,m)] = 0
                else:
                    x1 = graph[(i-1,j,m)]
                    x2 = graph[(i, j-1, m)]
                    x3 = graph[(i, j, m-1)]
                    x4 = graph[(i-1, j-1, m)]
                    x5 = graph[(i-1, j, m-1)]
                    x6 = graph[(i, j-1, m-1)]
                    match = graph[(i-1, j-1, m-1)] + 1
                    nomatch = graph[(i-1, j-1, m-1)]
                    if a[i-1] == b[j-1] == c[m-1]:
                        graph[i,j,m] = max(x1,x2,x3,x4,x5,x6, match)
                    else:
                        graph[i,j,m] = max(x1,x2,x3,x4,x5,x6, nomatch)
    return graph[(len(a),len(b), len(c))]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
