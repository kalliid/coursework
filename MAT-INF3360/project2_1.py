def solver(f):
    n = len(f)-2
    h = 1./(n+1)
    u = zeros(n+2)
    a = zeros(n+2)
    b = zeros(n+2)

    for i in range(n+1):
        a[i+1] = a[i] + h*(f[i] + 2*f[])


