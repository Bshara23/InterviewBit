

def anytwo(A):
    tab = [[0 for i in range(len(A) + 1)] for j in range(len(A) + 1)]
    for i in range(1, len(A) + 1):
        for j in range(1, len(A) + 1):
            if i != j and (A[i - 1] == A[j - 1]):
                tab[i][j] = 1 + tab[i - 1][j - 1]
                if tab[i][j] >= 2:
                    return 1
            else:
                tab[i][j] = max(tab[i - 1][j], tab[i][j - 1])
    return 0



A = "abba"
print(anytwo(A))
