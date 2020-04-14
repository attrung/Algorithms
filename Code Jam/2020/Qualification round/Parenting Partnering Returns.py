# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 03:18:08 2020

@author: John Nguyen
"""

import numpy

t = int(input())

for x in range(t):
    n = int(input())
    start_time = []
    end_time = []
    for j in range(n):
        row = [int(p) for p in input().split()]
        start_time.append(row[0])
        end_time.append(row[1])
    order = numpy.argsort(start_time)
    Cam = [0]*1440
    Jam = [0]*1440
    ans = [None]*n
    possible = True
    for i in order:
        start = start_time[i]
        end = end_time[i]
        if sum(Cam[start:end]) == 0:
            Cam[start:end] = [1]*(end - start)
            ans[i] = "C"
        else:
            if sum(Jam[start:end]) == 0:
                Jam[start:end] = [1]*(end - start)
                ans[i] = "J"
            else:
                possible = False
    
    if possible == False:
        print("Case #{}: ".format(x + 1) + "IMPOSSIBLE")
    
    else:
        ans = ''.join(ans)
        print("Case #{}: ".format(x + 1) + ans)