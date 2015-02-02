def Fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fib(n-1) + Fib(n-2)

for i in range(1,41):
    print Fib(i)