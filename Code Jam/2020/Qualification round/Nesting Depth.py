# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 02:44:02 2020

@author: John Nguyen
"""

t = int(input())

for k in range(t):
    S = input()
    s = []
    for j in S:
        s.append(int(j))
    no_p = 0
    answer = []
    for x in s:
        if x == no_p:
            answer.append(str(x))
        elif x > no_p:
            add = x - no_p
            for m in range(add):
                answer.append('(')
                no_p += 1
            answer.append(str(x))
        elif x < no_p:
            add = no_p - x
            for m in range(add):
                answer.append(')')
                no_p -= 1
            answer.append(str(x))
    for i in range(no_p):
        answer.append(')')
    
    answer = ''.join(answer)
    print('Case #{}: '.format(k+1) + answer)
    
    