def get_diagonal(n, k):
    if n%2 == 0:
        if k%2 == 0:
            if k > 3*n -1:
                B = int((k-2*n +2)/(n-2))
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
                B = round(int(k-2*A - n + 1)/(n-3))
                C = int(k - 2*A - B*(n-3))
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

n = int(input())
k = int(input())
# for i in range(n+2, n**2 -1):
#     print(i)
#    print(get_diagonal(n,i))
print(get_diagonal(n, k))