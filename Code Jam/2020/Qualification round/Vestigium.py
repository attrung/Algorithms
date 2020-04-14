# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 02:17:59 2020

@author: John Nguyen
"""
import numpy

t = int(input())

def check_repeat(a):
    count = [0]*len(a)
    for x in a:
        count[x-1] = count[x-1] + 1
    if 0 not in count:
        return True
    return False

for x in range(t):
    n = int(input())
    matrix = []
    k = 0
    r = 0
    c = 0
    for j in range(n):
        row = [int(i) for i in input().split()]
        if check_repeat(row) == False:
            r += 1
        k += row[j]
        matrix.append(row)
    matrix = numpy.transpose(matrix)
    for row in matrix:
        if check_repeat(row) == False:
            c += 1
    print("Case #{}: {} {} {}".format(x + 1, k, r, c))

