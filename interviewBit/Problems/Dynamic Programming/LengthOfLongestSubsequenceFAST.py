# https://docs.python.org/2/library/bisect.html

"""

This module provides support for maintaining a list in sorted order without having to sort the list
after each insertion. For long lists of items with expensive comparison operations,
this can be an improvement over the more common approach.
The module is called bisect because it uses a basic bisection algorithm to do its work.

O(log(n))
"""


from bisect import bisect_left

# Time Complexity: O(n log(n)) !!
def longestSubsequenceLength(A):
    h1, h2 = [], []
    for x in A:  # O(n)
        i = bisect_left(h1, x)  # O(log(n))
        if i >= len(h1):
            h1.append(x)
        else:
            h1[i] = x

        # if h1 is empty then set j to 0, otherwise do like above
        j = bisect_left(h2, -x, len(h1) - 1) if h1 else 0  # O(log(n))
        if j >= len(h2) or len(h2) < len(h1):
            h2.append(-x)
        else:
            h2[j] = -x
    return len(h2)


A = [1, 11, 2, 10, 4, 5, 2, 1]
print(longestSubsequenceLength(A))


