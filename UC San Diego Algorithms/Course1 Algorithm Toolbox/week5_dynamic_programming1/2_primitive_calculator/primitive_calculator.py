# Uses python3
import sys

def optimal_sequence(n):
    n += 1
    least = [0, 1]
    sequence = [[0], [0,1]]
    for i in range(1,n):
        x = i + 1
        pre_val = {3: x, 2: x, 1: x-1}
        for j in range(2,4):
            if pre_val[j] % j == 0:
                pre_val[j] = int(pre_val[j]/j)
            else:
                del pre_val[j]
        
        val = []
        k = []
        for m in pre_val.keys():
            val.append(least[pre_val[m]])
            k.append(m)
            
        minimum = min(val)
        
        index = val.index(minimum)        
        divide_type = k[index]
        new_sequence = sequence[pre_val[divide_type]].copy()
        new_sequence.append(x)
        sequence.append(new_sequence)
        least.append(len(new_sequence) - 1)
    return sequence[n-1][1:]
        
        
        
input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
