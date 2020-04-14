#Uses python3

import sys

def compare(x,y):
    x = str(x)
    y = str(y)
    n = max(len(x), len(y))
    if len(x) < n:
        temp = x
        m = len(x)
        p = n//m
        q = n -m*p
        for i in range(p-1):
            x += temp
        x += x[0:q]
    if len(y) < n:
        temp = y
        m = len(y)
        p = n//m
        q = n -m*p
        for i in range(p-1):
            y += temp
        y += y[0:q]
    return x > y

def largest_number(a):
    res = ""
    a = [int(i) for i in a]
    while a != []:
        val = None
        maxDigit = -1
        for i in range(len(a)):
            if compare(a[i],maxDigit):
                maxDigit = a[i]
                val = i
        res += str(maxDigit)
        a.pop(val)
    return res

#if __name__ == '__main__':
#    input = sys.stdin.read()
#    data = input.split()
#    a = data[1:]
#    print(largest_number(a))
    
data = ['2', '4', '1', '1',
 '10',
 '1',
 '3',
 '10',
 '2',
 '100',
 '1']
print(largest_number(data))
