# Uses python3
def edit_distance(s, t):
    graph = {}
    graph[(0,0)] = 0
    for i in range(0, len(s) + 1):
        for j in range(0, len(t) + 1):
            if i == 0 and j == 0:
                pass
            elif i == 0 and j != 0:
                graph[(0,j)] = graph[(0,j-1)] + 1
            elif j == 0 and i != 0:
                graph[(i,0)] = graph[(i-1,0)] + 1
            else:
                right = graph[(i-1, j)] + 1
                down = graph[(i, j-1)] + 1
                match = graph[(i - 1, j - 1)]
                nomatch = graph[(i-1, j-1)] + 1
                if s[i-1] == t[j-1]:
                    graph[(i, j)] = min(right, down, match)
                else:
                    graph[(i, j)] = min(right, down, nomatch)
    return graph[(len(s), len(t))]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
