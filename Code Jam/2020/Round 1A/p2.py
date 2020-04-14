import math
t = int(input())

# depth = 29
# pascal_triangle = []
# for i in range(depth + 1):
#     pascal_triangle.append([])
# for i in range(depth + 1):
#     for j in range(i + 1):
#         pascal_triangle[i].append(math.factorial(i)/(math.factorial(j) * math.factorial(i-j)))

def get_consitute(n):
    list_stuff = []
    a = int(math.log(n, 2))
    if n - a < 2**a:
        a = a - 1
    n = n - a - 2**a + 1
    list_stuff.append(a + 1)
    for i in range(a-1, -1, -1):
        if 2**i < n:
            n = n + 1 - 2 ** i
            list_stuff.append(i + 1)
    return list_stuff, n-1

def create_walk(row, n):
    walk = [(1,1)]
    left = True
    for i in range(2, max(row) + 1):
        if i not in row and left:
            walk.append((i,1))
        elif i not in row and not left:
            walk.append((i, i))
        else:
            if left:
                for j in range(1, i+1):
                    walk.append((i, j))
                left = False
            else:
                for j in range(i, 0, -1):
                    walk.append((i, j))
                left = True
    for i in range(max(row) + 1, max(row) + 1 + n):
        if left:
            walk.append((i, 1))
        else:
            walk.append((i, i))
    return walk

for o in range(t):
    n = int(input())
    row, n = get_consitute(n)
    walk = create_walk(row, n)
    print('Case #{}:'.format(o+1))
    for item in walk:
        print(' '.join(str(i) for i in item))

