# python3

import sys
import threading

def find_height(root, all_nodes, height = 0):
    height += 1
    if all_nodes[root] == []:
        return height
    else:    
        child = all_nodes[root]
        all_val = []
        for i in child:
            all_val.append(find_height(i, all_nodes, height))
        height = max(all_val)
        return height

def compute_height(n, parents):
    all_nodes = []
    for i in range(n):
        all_nodes.append([])
    root = 0
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            all_nodes[parents[i]].append(i)
    # Replace this code with a faster implementation
    max_height = find_height(root, all_nodes, 0)
    return max_height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
