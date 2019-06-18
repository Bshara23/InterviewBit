import math
from pip._internal import main
main(["install", "pip"])

def binom(x, y):

    if x == 1 or y == 1:
        return 1

    x -= 1
    y -= 1
    a = math.factorial(x)
    b = math.factorial(y)
    c = math.factorial(x + y)  # that appears to be useful to get the correct result
    return c // (b * a)

print(binom(15 - 1, 9 - 1))