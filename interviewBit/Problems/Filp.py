
def f(A):

    length = len(A)
    maxI = maxV = minI = 0
    B = M = N = [0] * length
    for i in range(length):
        B[i] = 1 if A[i] == '0' else -1

    maxV = M[0] = B[0]
    for i in range(1, length):
        M[i] = M[i-1] + B[i] if M[i-1] + B[i] > B[i] else B[i]
        maxV = max(maxV, M[i])

    for i in range(0, length):
        print(M[i])

    for i in range(0, length):
        if maxV == M[i] and M[i] > 0:
            maxI = i
            break

    minI = 0
    # go back and find the first index
    for i in range(maxI, -1, -1):
        if M[i] > 0:
            minI = i
            break

    if maxV < 0: return []
    return [minI + 1, maxI + 1]


A = "0111000100010"

print(f(A))

