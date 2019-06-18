#https://www.interviewbit.com/problems/max-sum-without-adjacent-elements/
import numpy as np

def adjacent(A=[]):
    n = len(A[0])
    if n == 0:
        return 0
    dp = [0] * n
    dp[0] = max(A[0][0], A[1][0])
    if n == 1:
        return dp[0]
    dp[1] = max(dp[0], A[0][1], A[1][1])
    for i in range(2, n):
        # recursive function
        dp[i] = max((dp[i - 2] + max(A[0][i], A[1][i])), dp[i - 1])

    # print(dp)
    return dp[n - 1]

A = [
  [16, 5, 54, 55, 36, 82, 61, 77, 66, 61],
  [31, 30, 36, 70, 9, 37, 1, 11, 68, 14]]
print(adjacent(A))
