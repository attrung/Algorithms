# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
    key: 
        1: first list
        2: complement list
        3: flip list
        4: both
"""

import sys
import numpy as np
t, b = [int(x) for x in input().split()]

def complement(x):
   k = x.copy()
   for i in range(len(k)):
       if k[i] == None:
           pass
       elif k[i] == 1:
           k[i] = 0
       else:
           k[i] = 1
   return k


for o in range(t):
   if b == 10:
       ans = [None] * 10
       for i in range(1, 11):
           print(i)
           ans[i - 1] = int(input())

       answer = ''.join(str(j) for j in ans)

       print(answer)

       correct = str(input())
       if correct == 'Y':
           continue

       elif correct == 'N':
           sys.exit(-1)




   if b == 20:
       ans = [[None] * 20] * 4

       for i in range(1, 11):
           j = 5 + i
           print(j)
           ans[0][j - 1] = int(input())

       ans[1] = complement(ans[0])
       ans[2] = list(np.flip(ans[0]))
       ans[3] = complement(ans[2])

       temp_ans = []
       for i in range(11, 21):
           if 11 <= i <= 15:
               print(i - 10)
           else:
               print(i)
           temp_ans.append(int(input()))

       possible_out = []
       possible_out.append(temp_ans)
       possible_out.append(complement(temp_ans))
       possible_out.append(list(np.flip(temp_ans)))
       possible_out.append(list(np.flip(complement(temp_ans))))

       temp_ans = []
       for i in range(21, 31):
           print(i - 20)
           temp_ans.append(int(input()))

       if temp_ans[:5] == possible_out[0][:5]:
           out = possible_out[0]
       elif temp_ans[:5] == possible_out[1][:5]:
           out = possible_out[1]
       elif temp_ans[:5] == possible_out[2][:5]:
           out = possible_out[2]
       elif temp_ans[:5] == possible_out[3][:5]:
           out = possible_out[3]
       
       for i in range(0, 4):
           ans[i][0:5] = out[0:5]
           ans[i][15:20] = out[5:10]    
           
       if temp_ans[5:10] == ans[0][5:10]:
           final_ans = ans[0]
       elif temp_ans[5:10] == ans[1][5:10]:
           final_ans = ans[1]
       elif temp_ans[5:10] == ans[2][5:10]:
           final_ans = ans[2]
       elif temp_ans[5:10] == ans[3][5:10]:
           final_ans = ans[3]

       final_ans = [str(p) for p in final_ans]
       answer = ''.join(final_ans)
       print(answer)

       correct = str(input())
       if correct == 'Y':
           continue

       elif correct == 'N':
           sys.exit(-1)
