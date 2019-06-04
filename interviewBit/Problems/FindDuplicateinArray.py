

def f(A):

    B = [0] * len(A)
    for i in range(len(A)):
        B[A[i]] += 1

        if (B[A[i]] == 2):
            return A[i]
    return 0


A = [1, 2, 4, 5, 4, 1]
print(f(A))