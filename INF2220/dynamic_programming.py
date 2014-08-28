memo = {}
def fib_memo(n):
    if n in memo: 
        return memo[n]
    else:
        memo[n] = n if n < 2 else fib_memo(n-1) + fib_memo(n-2)
        return memo[n]

def memoize(f):
    cache = {}
    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorated_function

@memoize
def fib(n):
    return n if n < 2 else fib(n-2) + fib(n-1)

print fib_memo(100)
#print fib(100)
