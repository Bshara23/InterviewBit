#https://www.interviewbit.com/problems/equal-average-partition/

# couldn't solve it, solution based of interviewBit.com
from functools import wraps
import fractions

def memo(f):
    cache = {}

    @wraps(f)
    def wrap(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return wrap


class Solution:
    # @param A : list of integers
    # @return a list of list of integers

    @memo
    def knapsack(self, i, num, tot):
        # Find num items in A that add up to tot
        if i > len(self.A) - 1 or num <= 0 or tot <= 0:
            return None
        elif num == 1 and self.A[i] == tot:
            return [self.A[i]]
        else:
            include = self.knapsack(i + 1, num - 1, tot - self.A[i])
            exclude = self.knapsack(i + 1, num, tot)

            if include:
                return [self.A[i]] + include
            elif exclude:
                return exclude

    def avgset(self, A):
        tot = sum(A)
        n = len(A)

        gcd = fractions.gcd(tot, n)

        num = n // gcd
        self.A = sorted(A)

        for i in range(num, n // 2 + 1, num):
            k = self.knapsack(0, i, tot * i // n)
            if k is not None:
                temp = k[:]
                return [k, [i for i in self.A if not i in temp or temp.remove(i)]]
        return []