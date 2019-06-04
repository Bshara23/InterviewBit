
def wave(A):

    A.sort()

    if (len(A) % 2 == 0):
        length = len(A)
    else:
        length = len(A) - 1
    for i in range(0, length, 2):
        A[i], A[i+1] = A[i+1], A[i]

    return A


B = [1, 2, 3, 4]
print(wave(B))

