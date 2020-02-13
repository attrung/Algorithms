# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 15:25:42 2020

@author: John Nguyen
"""
def max_slice2(M,data): #Dynamic Programming
    M = int(M)
    n = len(data)
    weight_up = [0]*(M+1)
    weight_down = [0]*(M+1)
    series_up = [[]]*(M+1)
    series_down = [[]]*(M+1)
    for i in range(1, n+1):
        weight_up = weight_down.copy()
        weight_down = [0]*(M + 1)
        series_up = series_down.copy()
        series_down = [[]]*(M + 1)
        for j in range(0, M+1):
            val = int(data[i-1])
            weight_down[j] = weight_up[j]
            series_down[j] = series_up[j].copy()
            if val <= j:
                if weight_down[j] <= weight_up[j-val] + val:
                    weight_down[j] = weight_up[j-val] + val
                    series_down[j] = series_up[j-val].copy()
                    series_down[j].append(val)
    return weight_down[-1], series_down[-1]

def max_slice(M,data): #Greedy
    plate = []
    val = 0
    M = int(M)
    data.reverse()
    while val < M - 150000:
        plate.append(data[0])
        val += data[0]
        data.pop(0)
    #first use greedy, then switch to dynamic programming
    max_weight, series = max_slice2(M-val, data)
    return val + max_weight, plate + series

def return_index(data, ans):
    index = []
    for i in ans:
        a = data.index(i)
        index.append(a)
        data[a] = None
    return index
        

#import data
org = open("e_also_big.in","r")
org = org.read()
org = org.split()
M = org[0]
data = org[2:]
new_data = []
for x in data:
    new_data.append(int(x))
data = new_data.copy()

#run program
ans, dat = max_slice(str(int(M)), data)
print(ans)
print(dat)
dat = return_index(new_data, dat)

fh = open("submit/e_submit.txt", "w")
fh.write(str(len(dat)))
fh.write("\n")
fh.write(' '.join(str(i) for i in dat)) 
fh.close()

