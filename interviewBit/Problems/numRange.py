def findSumLessThan(A, k):
    cnt = start = end = 0
    sum = A[0]
    arrSize = len(A)

    while start < arrSize and end < arrSize:
        if sum < k:
            end += 1
            if start <= end:
                cnt += end - start
            if end < arrSize:
                sum += A[end]
        else:
            sum -= A[start]
            start += 1
    return cnt

def numRange(A, B, C):

    print(findSumLessThan(A, C))
    print(findSumLessThan(A, B))
    return findSumLessThan(A, C) - findSumLessThan(A, B)


A = [ 76, 22, 81, 77, 95, 23, 27, 35, 24, 38, 15, 90, 19, 46, 53, 6, 77, 96, 100, 85, 43, 16, 73, 18, 7, 66 ]
B = 98
C = 290

print(numRange(A, B, C))


