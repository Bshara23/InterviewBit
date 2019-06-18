

import math as mt
def primesum(A):

    if A <= 1:
        return []

    def isPrime(x):
        for i in range(2, int(mt.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

    if isPrime(A):
        return []

    for i in range(2, (A // 2) + 1):
        if isPrime(i) and isPrime(A - i):
            return [i, A - i]




print(primesum(4))