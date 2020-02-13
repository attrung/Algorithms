#Uses python3

import sys

def lcs2(a, b):
    graph = {}
    for i in range(len(a)+1):
        for j in range(len(b)+1):
            if i == 0 or j == 0:
                graph[(i,j)] = 0
            else:
                right = graph[(i, j - 1)]
                down = graph[(i - 1, j)]
                match = graph[(i-1, j-1)] + 1
                nomatch = graph[(i-1, j -1)]
                if a[i-1] == b[j-1]:
                    graph[i,j] = max(right, down, match)
                else:
                    graph[i,j] = max(right, down, nomatch)
    return graph[(len(a),len(b))]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
