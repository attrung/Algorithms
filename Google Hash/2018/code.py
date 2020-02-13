# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 07:40:12 2020

@author: John Nguyen
"""
class graph():
    def __init__(R, C, B, T, F):
        self.r = R
        self.c = C
        self.bonus = B
        self.step = T
        self.car = F
        
class car(graph):
    def __init__():
        self.pos = (0,0)

    def move(loc):
        dis = abs(loc[0] - self.pos[0]) + abs(loc[1] - self.pos[1])
        self.loc = (loc)
        aval = False
        return dis
    
    def arrive():
        aval = True
        self.pos = loc.copy()
        
class cus(graph):
    def __init__(start, end, time):
        self.start = start
        self.end = end
        self.s_time = time[0]
        self.e_time = time[1]
    
def main():
    graph = graph(R, C, B, T, F)
    list_car = []
    for t in range(0, graph.step):
        for c in range(0, graph.c):
            list_car.append(car(graph))
         
    
    

org = open("a.in","r")
org = org.read()
org = org.split("\n")
R, C, F, N, B, T = [int(j) for j in org[0].split()]
start = []
end = []
time = []
for i in range(1, N+1):
    a, b, x, y, s, f = org[i].split()
    start.append((a,b))
    end.append((x,y))
    time.append((s,f))
