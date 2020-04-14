#Uses python3

import sys

def change(x,n):
    m = len(x)
    y = x
    if m < n:
        p = n//m
        q = n -m*p
        for i in range(p-1):
            x += y
        x += x[0:q]
        return x
    else:
        return x

def largest_number(a):
    #write your code here
    answer = ""
    x = a.copy()
    a = [int(i) for i in a]
    y = []
    for i in x:
        y.append(change(i,4))
    index = sorted(range(len(y)), key = y.__getitem__, reverse = True)
    for i in index:
        answer += str(x[i])
    return answer

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

#    for i in x:
#        y.append(change(i,n))
#    index = sorted(range(len(y)), key = y.__getitem__, reverse = True)
#    for i in index:
#        answer += str(x[i])
#    return answer