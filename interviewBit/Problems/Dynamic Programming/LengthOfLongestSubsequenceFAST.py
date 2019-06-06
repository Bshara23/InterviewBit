
from bisect import bisect_left

def longestSubsequenceLength(A):
    h1, h2 = [], []
    for x in A:
        i = bisect_left(h1, x)
        if i >= len(h1):
            h1.append(x)
        else:
            h1[i] = x

        j = bisect_left(h2, -x, len(h1) - 1) if h1 else 0
        if j >= len(h2) or len(h2) < len(h1):
            h2.append(-x)
        else:
            h2[j] = -x
    return len(h2)


A = [1, 11, 2, 10, 4, 5, 2, 1]
print(longestSubsequenceLength(A))