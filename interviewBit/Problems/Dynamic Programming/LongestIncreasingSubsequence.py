
def lis(A):

    len_a = len(A)
    if len_a == 0:
        return 0

    M = [1] * len_a
    for i in range(len_a - 2, -1, -1):
        for j in range(i + 1, len_a):
            if A[j] > A[i]:
                M[i] = max(M[i], M[j] + 1)

    return max(M)


A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

print(lis(A))
