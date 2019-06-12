# https://www.interviewbit.com/problems/ways-to-decode/
def numDecodings(A):

    if A[0] == '0':
        return 0
    M = [0] * (len(A) + 1)
    M[0] = 1
    M[1] = 1
    for i in range(1, len(A)):
        g = int(A[i - 1] + A[i])
        if A[i] == '0' and (g != 10 and g != 20):
            return 0
        elif g == 10 or g == 20:
            M[i + 1] = M[i - 1]
        elif 10 < g <= 26:
            M[i + 1] = M[i] + M[i - 1]
        else:
            M[i + 1] = M[i]

    return M[-1]


A = "5163490394499093221199401898020270545859326357520618953580237168826696965537789565062429676962877038781708385575876312877941367557410101383684194057405018861234394660905712238428675120866930196204792703765204322329401298924190"
print(numDecodings(A))