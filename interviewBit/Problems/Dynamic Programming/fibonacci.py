
# assuming that n <= 100
memo = [0] * 100

def fib(n):

    if n <= 1:
        return n

    if memo[n] == 0:
        memo[n] = fib(n - 1) + fib(n - 2)

    return memo[n]

print(fib(9))
