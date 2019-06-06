

#O(n^2)
def maxSeq(A):

    lenA = len(A)
    M = [0] * lenA
    M[0] = 1

    for i in range(lenA):
        max_length = 0
        for j in range(lenA):
            if M[j] > max_length and A[j] < A[i]:
                max_length = M[j]
        M[i] = max_length + 1

    return M

#O(n^2)
def longestSubsequenceLength(A):

    if len(A) == 0:
        return 0
    inc = maxSeq(A)
    dec = maxSeq(A[::-1])[::-1]

    max_length = 0
    for i in range(len(inc)):
        for j in range(i, len(inc)):
            if inc[i] + dec[j] - 1 > max_length:
                max_length = inc[i] + dec[j] - 1

    return max_length

# total O(n^2)

A = [ 1, 2 ]

#print(A)
#print(maxSeq(A))
#print(maxSeq(A[::-1])[::-1])
print(longestSubsequenceLength(A))

