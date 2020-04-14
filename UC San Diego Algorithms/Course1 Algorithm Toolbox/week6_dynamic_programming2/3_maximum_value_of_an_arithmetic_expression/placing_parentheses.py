# Uses python3
import math

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False   
        
def find_maxmin(a_max, a_min, b_max, b_min, op):
    val1 = evalt(a_max, b_max, op)
    val2 = evalt(a_max, b_min, op)
    val3 = evalt(a_min, b_max, op)
    val4 = evalt(a_min, b_min, op)
    return max([val1, val2, val3, val4]), min([val1, val2, val3, val4])
    
    
def get_maximum_value(dataset):
    graph_max = {}
    graph_min = {}
    n_num = int((len(dataset) + 1)/2)
    #making list of numbers:
    list_num = []
    for i in range(len(dataset)):
        if i%2 == 0:
            list_num.append(int(dataset[i]))
    #making list of operations:
    list_op = []
    for i in range(len(dataset)):
        if i%2 == 1:
            list_op.append(dataset[i])
    
    #actual calculation:
    for i in range(0, n_num):
        for j in range(0, n_num - i):
            if i == 0:
                graph_max[(j,j)] = list_num[j]
                graph_min[(j,j)] = list_num[j]
            else:
                graph_max[(j, j+i)] = - math.inf
                graph_min[(j, j+i)] = math.inf
                for k in range(j, j + i):
                    max_cal, min_cal = find_maxmin(graph_max[(j, k)], 
                    graph_min[(j,k)], graph_max[(k+1, j+i)], graph_min[(k+1,j+i)], list_op[k])
                    if max_cal > graph_max[(j, j+i)]:
                        graph_max[(j, j+i)] = max_cal
                    if min_cal < graph_min[(j, j + i)]:
                        graph_min[(j, j+i)] = min_cal
            
    return graph_max[(0, n_num-1)]


if __name__ == "__main__":
    print(get_maximum_value(input()))
