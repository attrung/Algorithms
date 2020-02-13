# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 16:42:32 2020

@author: John Nguyen
"""
def find_loc(i, j, W):
    return (W+1)*i + j

def max_slice(M,data):
    M = int(M)
    n = len(data)
    max_weight = {}
    series = {}
    for i in range(n+1):
        for j in range(0, M+1):
            if i == 0 or j == 0:
                max_weight[find_loc(i,j,M)] = 0
                series[find_loc(i,j,M)] = []
            else:
                val = int(data[i-1])
                max_weight[find_loc(i,j,M)] = max_weight[find_loc(i-1,j,M)]
                series[find_loc(i,j,M)] = series[find_loc(i-1,j,M)].copy()
                if val < j:
                    if max_weight[find_loc(i,j,M)] < max_weight[find_loc(i-1, j-val, M)] + val:
                        max_weight[find_loc(i,j,M)] = max_weight[find_loc(i - 1, j - val, M)] + val
                        series[find_loc(i,j,M)] = series[find_loc(i - 1, j - val, M)].copy()
                        series[find_loc(i,j,M)].append(val)
    return max_weight[find_loc(n, M, M)], series[find_loc(n, M, M)]
            
#import data
org = open("a_example.in","r")
org = org.read()
org = org.split()
M = org[0]
data = org[2:]

#run program
print(max_slice(M, data))

