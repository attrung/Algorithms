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


n = int(input())
k = int(input())
print(get_general_format(n, k))