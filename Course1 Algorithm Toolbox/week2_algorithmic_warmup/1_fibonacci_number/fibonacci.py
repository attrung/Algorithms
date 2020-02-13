# Uses python3
def calc_fib(n):
    if n <= 1:
        return n
    else:
        fib = [1,1]
        for i in range(2,n):
            fib.append(fib[i-1]+fib[i-2])
        return fib[-1]

n = int(input())
print(calc_fib(n))
