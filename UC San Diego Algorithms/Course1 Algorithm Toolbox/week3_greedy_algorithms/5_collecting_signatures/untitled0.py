# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 15:59:53 2019

@author: John Nguyen
"""

def optimal_points(segments):
    low = []
    high = []
    #write your code here
    for s in segments:
        low.append(s[0])
        high.append(s[1])
    index = sorted(range(len(high)),key = high.__getitem__)
    points = []
    while True:
        a = high[index[0]]
        points.append(a)
        i = 0
        while i < len(index):
            if low[index[i]] <= a <= high[index[i]]:
                index.pop(i)
            else:
                i += 1
        if index == []:
            break
    return points