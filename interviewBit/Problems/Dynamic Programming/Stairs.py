
# https://www.interviewbit.com/problems/stairs/
# learned based off:
# https://web.stanford.edu/class/cs97si/04-dynamic-programming.pdf

"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example :

Input : 3
Return : 3

Steps : [1 1 1], [1 2], [2 1]

"""


def climbStairs(A):

    if A < 0:
        return 0
    if A == 0:
        return 1
    if A == 1:
        return 1

    D = [0] * (A + 1)
    D[0] = 1
    D[1] = 1

    for i in range(2, A + 1):
        D[i] = D[i - 1] + D[i - 2]

    return D[A]

print(climbStairs(5))