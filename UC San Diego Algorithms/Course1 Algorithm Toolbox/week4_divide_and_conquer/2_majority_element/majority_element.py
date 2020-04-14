# Uses python3
import sys

def get_majority_element(a):
    mid = (0 + len(a))//2
    if len(a) == 1:
        return [True, a[0]]
    else:
        x = get_majority_element(a[0:mid])
        y = get_majority_element(a[mid:len(a)])
        if x[0]:
            k = 0
            for i in range(len(a)):
                if a[i] == x[1]:
                    k += 1
            if k > mid:
                return [True, x[1]]
            else:
                x[0] = False
        if y[0]: 
            k = 0
            for i in range(len(a)):
                if a[i] == y[1]:
                    k += 1
            if k > mid:
                return [True, y[1]]
            else:
                y[0] = False
        if x[0] == False and y[0] == False:
            return [False, -1]

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a)[0]:
        print(1)
    else:
        print(0)
