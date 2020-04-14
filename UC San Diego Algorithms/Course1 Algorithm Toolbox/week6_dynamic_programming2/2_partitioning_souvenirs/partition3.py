# Uses python3
import sys

def result(A):
    W = sum(A)/3
    if W % 1 != 0:
        return 0
    else:
        W = int(W)
        time1, A = partition(A,W)
        time2, A = partition(A,W)
    if time1 == 1 and  time2 == 1:
        return 1
    else:
        return 0
    
def partition(A, W):
    W += 1
    possible = [1]
    weights = {0: []}
    for i in range(1,W):
        weights[i] = []
    for i in range(1,W):
        for j in range(len(A)):
            if A[j] <= len(possible):
                if possible[i - A[j]] == 1:
                    if j not in weights[i-A[j]]:
                        possible.append(1)
                        weights[i] = weights[i-A[j]].copy()
                        weights[i].append(j)
                        break
            if j == len(A)-1:
                possible.append(0)
                break
    for item in weights[W-1]:
        A.pop(item)
    return possible[-1], A

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(result(A))

