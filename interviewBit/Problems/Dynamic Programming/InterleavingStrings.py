
def isInterleave(A, B, C):

    len_a, len_b, len_c = map(len, [A, B, C])

    if len_a + len_b != len_c:
        # length mismatch
        return False

    def rec(i, j, k, mem={}):

        # if reached the end
        if i == len_a and j == len_b:
            return True

        # if this value has been calculated before then return it
        if (i, j) in mem:
            return mem[(i, j)]

        # check if we can take the right/left path then take it
        res = (i < len_a and A[i] == C[k] and rec(i+1, j, k+1)) or\
              (j < len_b and B[j] == C[k] and rec(i, j+1, k+1))

        # memoize the result
        mem[(i, j)] = res
        return res

    return rec(0, 0, 0)



A = "aabcc"
B = "dbbca"
C1 = "aadbbcbcac"
C2 = "aadbbbaccc"

print(isInterleave(A, B, C1))
print(isInterleave(A, B, C2))