# Uses python3
import sys

def find_loc(i, j, W):
    return (W+1)*i + j

def optimal_weight(W, w):
    n = len(w)
    graph = [None] * ((n+1) * (W+1))
    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                graph[find_loc(i, j, W)] = 0
            else:
                graph[find_loc(i, j, W)] = graph[find_loc(i - 1, j, W)]
                if w[i-1] <= j:
                    val = graph[find_loc(i-1, j - w[i-1], W)] + w[i-1]
                    if graph[find_loc(i, j, W)] < val:
                        graph[find_loc(i, j, W)] = val
    return graph[find_loc(n, W, W)]
                
if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
