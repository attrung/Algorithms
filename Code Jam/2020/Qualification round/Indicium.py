t = int(input())

import numpy as np

def get_general_format(n, k):
    if n%2 == 1:
        format = [[1,3,5,4,2], [3,2,4,1,5], [5,1,2,3,4], [4,5,1,2,3], [2,4,3,5,1]]
        for i in range(5 + 2, n + 2, 2):
            new_format = []
            for j in range(i):
                new_format.append([None] * i)
            for m in range(len(new_format)):
                if m == 0 or m == i-1:
                    new_format[m][m] = 1
                else:
                    new_format[m][m] = 2
            for column in range(2, i-1):
                for row in range(i):
                    new_format[column][row] = (new_format[column][column] + row - column)%i
                    if new_format[column][row] == 0:
                        new_format[column][row] = i

            # last column
            new_format[-1][:-3] = format[-1][:-1]
            new_format[-1][-1] = 1
            new_format[-1][-2] = i - 1
            new_format[-1][-3] = i

            # first column
            new_format[0][:-3] = format[0][:-1]
            new_format[0][-1] = 2
            new_format[0][-2] = i
            new_format[0][-3] = i-1

            # second column
            new_format[1][:-4] = format[1][:-2]
            new_format[1][-1] = i
            new_format[1][-2] = 1
            new_format[1][-3] = i - 2
            new_format[1][-4] = i -1
            format = new_format

    if n%2 == 0:
        if k %2 == 0:
            format = [[1,3,4,2],[3,2,1,4],[4,1,2,3],[2,4,3,1]]
            for i in range(4 + 2, n + 2, 2):
                new_format = []
                for j in range(i):
                    new_format.append([None] * i)
                for m in range(len(new_format)):
                    if m == 0 or m == i -1:
                        new_format[m][m] = 1
                    else:
                        new_format[m][m] = 2
                for column in range(2, i - 1):
                    for row in range(i):
                        new_format[column][row] = (new_format[column][column] + row - column) % i
                        if new_format[column][row] == 0:
                            new_format[column][row] = i

                # last column
                new_format[-1][:-3] = format[-1][:-1]
                new_format[-1][-1] = 1
                new_format[-1][-2] = i - 1
                new_format[-1][-3] = i

                # first column
                new_format[0][:-3] = format[0][:-1]
                new_format[0][-1] = 2
                new_format[0][-2] = i
                new_format[0][-3] = i-1

                # second column
                new_format[1][:-4] = format[1][:-2]
                new_format[1][-1] = i
                new_format[1][-2] = 1
                new_format[1][-3] = i - 2
                new_format[1][-4] = i -1
                format = new_format

        else:
            format = [[1,4,3,2],[2,3,1,4],[4,1,2,3],[3,2,4,1]]
            for i in range(4 + 2, n + 2, 2):
                new_format = []
                for j in range(i):
                    new_format.append([None] * i)
                for m in range(len(new_format)):
                    if m == 0 or m == i - 1:
                        new_format[m][m] = 1
                    elif m == 1:
                        new_format[m][m] = 3
                    else:
                        new_format[m][m] = 2
                for column in range(2, i - 1):
                    for row in range(i):
                        new_format[column][row] = (new_format[column][column] + row - column) % i
                        if new_format[column][row] == 0:
                            new_format[column][row] = i

                # last column
                new_format[-1][:-3] = format[-1][:-1]
                new_format[-1][-1] = 1
                new_format[-1][-2] = i - 1
                new_format[-1][-3] = i

                # first column
                new_format[0][:-3] = format[0][:-1]
                new_format[0][-1] = 2
                new_format[0][-2] = i
                new_format[0][-3] = i-1

                # second column
                new_format[1][:-4] = format[1][:-2]
                new_format[1][-1] = i
                new_format[1][-2] = 1
                new_format[1][-3] = i - 2
                new_format[1][-4] = i -1
                format = new_format

    format = np.transpose(format)
    format = list(list(line) for line in format)

    return format


def get_diagonal(n, k):
    if n%2 == 0:
        if k%2 == 0:
            if k > 3*n -1:
                B = int((k-2*n + 1)/(n-2))
                A = int((k - B*(n-2))/2)
            else:
                B = 1
                A = int((k - B * (n - 2)) / 2)
            return(A, B)
        else:
            if k > 3*n:
                B = int((k-2*n -3)/(n-3))
                A = int((k - B*(n-3) - n + 2)/2)
                C = int(k - B*(n-3) - A*2)
            elif k < 2*n:
                A = 1
                B = int(k-2*A - n + 1)/(n-3)
                C = k - 2*A - B*(n-3)
            else:
                B = 1
                A = int((k - B*(n-3) - n + 2)/2)
                C = int(k - B*(n-3) - A*2)
            return(A,B,C)

    else:
        if k%2 == 0:
            if k > 3*n - 4:
                B = int((k-n)/(2*(n-2)))*2
                A = int((k - B*(n-2))/2)
            else:
                B = 2
                A = int((k - B*(n-2))/2)
            return (A,B)
        else:
            B = int(k/(2*(n-2)))*2 - 1
            A = int((k - B*(n-2))/2)
            return (A,B)

def nice_matrix(n,k):
    matrix = []
    for i in range(n):
        matrix.append([None]*n)

    for i in range(len(matrix)):
        matrix[i][i] = k/n

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = (matrix[i][i] + i - j) % n
            if matrix[i][j] == 0:
                matrix[i][j] = n
    return matrix

for o in range(t):
    n, k = [int(i) for i in input().split()]

# N = 2 _______________________________________________________
    if n == 2:
        if k == 3:
            ans = "IMPOSSIBLE"
            print("Case #{}: ".format(o + 1) + ans)
        else:
            ans = "POSSIBLE"
            k = int(k/2)
            matrix = [[k, 3-k], [3-k, k]]
            print("Case #{}: ".format(o + 1) + ans)
            for line in matrix:
                print(' '.join(str(int(x)) for x in line))
# N = 3 ________________________________________________________
    elif n == 3:
        if k != 3 and k != 6 and k != 9:
            ans = "IMPOSSIBLE"
            print("Case #{}: ".format(o + 1) + ans)
        else:
            ans = "POSSIBLE"
            k = int(k/3)
            matrix = [[2, 1, 0], [0, 2, 1], [1, 0, 2]]
            rest = [1,2,3]
            rest.remove(k)
            rest.append(k)
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    matrix[i][j] = rest[matrix[i][j]]
            print("Case #{}: ".format(o + 1) + ans)
            for line in matrix:
                print(' '.join(str(int(x)) for x in line))


# N = 4 _______________________________________________________
    elif n == 4:
        if k == 5 or k == 15:
            ans = "IMPOSSIBLE"
            print("Case #{}: ".format(o + 1) + ans)

        else:
            if k == 4 or k == 16:
                if k == 4:
                    format = [[1,2,3,4], [4,1,2,3], [3, 4, 1, 2], [2, 3, 4, 1]]
                else:
                    format = [[4, 1, 2, 3], [3, 4, 1, 2], [2, 3, 4, 1], [1, 2, 3, 4]]
                ans = "POSSIBLE"
                print("Case #{}: ".format(o +1) + ans)
                for line in format:
                    print(' '.join(str(int(x)) for x in line))

            elif k%2 == 0:
                format = [[1, 3, 4, 2], [3, 2, 1, 4], [4, 1, 2, 3], [2,4,3,1]]
                A, B = get_diagonal(n, k)
                if A == B:
                    matrix = nice_matrix(n, k)
                    ans = "POSSIBLE"
                    print("Case #{}: ".format(o + 1) + ans)
                    for line in matrix:
                        print(' '.join(str(int(x)) for x in line))

                else:
                    rest = [1,2,3,4]
                    rest.remove(A)
                    rest.remove(B)
                    x = [0, A, B] + rest
                    for i in range(len(format)):
                        for j in range(len(format[0])):
                            format[i][j] = x[format[i][j]]
                    ans = "POSSIBLE"
                    print("Case #{}: ".format(o +1) + ans)
                    for line in format:
                        print(' '.join(str(int(x)) for x in line))

            elif k%2 == 1:
                format = [[1, 2, 4, 3], [4,3,1,2], [3,1,2,4], [2,4,3,1]]
                A, B, C = get_diagonal(n, k)
                rest = [1,2,3,4]
                rest.remove(A)
                rest.remove(B)
                rest.remove(C)
                x = [0, A, B, C] + rest
                for i in range(len(format)):
                    for j in range(len(format[0])):
                        format[i][j] = x[format[i][j]]
                ans = "POSSIBLE"
                print("Case #{}: ".format(o +1) + ans)
                for line in format:
                    print(' '.join(str(int(x)) for x in line))

# N = 5 _______________________________________________________
    elif n == 5:
        if k == 6 or k == 24:
            ans = "IMPOSSIBLE"
            print("Case #{}: ".format(o + 1) + ans)
        else:
            if k == 5 or k == 25:
                matrix = nice_matrix(5, k)
                ans = "POSSIBLE"
                print("Case #{}: ".format(o + 1) + ans)
                for line in matrix:
                    print(' '.join(str(int(x)) for x in line))

            else:
                format = [[1,3,5,4,2], [4,2,1,5,3], [3,4,2,1,5], [5,1,3,2,4], [2,5,4,3,1]]
                A, B = get_diagonal(n, k)
                if A == B:
                    matrix = nice_matrix(n,k)
                    ans = "POSSIBLE"
                    print("Case #{}: ".format(o + 1) + ans)
                    for line in matrix:
                        print(' '.join(str(int(x)) for x in line))
                else:
                    rest = list(range(1, 6))
                    rest.remove(A)
                    rest.remove(B)
                    x = [0, A, B] + rest
                    for i in range(len(format)):
                        for j in range(len(format[0])):
                            format[i][j] = x[format[i][j]]
                    ans = "POSSIBLE"
                    print("Case #{}: ".format(o +1) + ans)
                    for line in format:
                        print(' '.join(str(int(x)) for x in line))

# other N _____________________________________________________________________________
    else:
        if k == n + 1 or k == n**2-1:
            ans = "IMPOSSIBLE"
            print("Case #{}: ".format(o + 1) + ans)
        else:
            format = get_general_format(n, k)

            if n%2 == 0 and k%2 == 1:
                A, B, C = get_diagonal(n, k)
                rest = list(range(1,n+1))
                rest.remove(A)
                rest.remove(B)
                rest.remove(C)
                x = [0, A, B, C] + rest
                for i in range(len(format)):
                    for j in range(len(format[0])):
                        format[i][j] = x[format[i][j]]
                ans = "POSSIBLE"
                print("Case #{}: ".format(o +1) + ans)
                for line in format:
                    print(' '.join(str(int(x)) for x in line))
            else:
                A, B = get_diagonal(n, k)
                if A == B:
                    matrix = nice_matrix(n, k)
                    ans = "POSSIBLE"
                    print("Case #{}: ".format(o + 1) + ans)
                    for line in matrix:
                        print(' '.join(str(int(x)) for x in line))
                else:
                    rest = list(range(1, n+1))
                    rest.remove(A)
                    rest.remove(B)
                    x = [0, A, B] + rest
                    for i in range(len(format)):
                        for j in range(len(format[0])):
                            format[i][j] = x[format[i][j]]
                    ans = "POSSIBLE"
                    print("Case #{}: ".format(o + 1) + ans)
                    for line in format:
                        print(' '.join(str(int(x)) for x in line))
