
# return the largest subset, if two subset has the maximal sum then return
# the one with the larger length (or the one with the larger number count)
# @param A : list of integers
    # @return a list of integers
def maxset(A):
    i = 0;
    maxi = -1;
    index = 0;
    a = []

    while i < len(A):
        while i < len(A) and A[i] < 0:
            i+=1
        l = []
        index = i
        while i < len(A) and A[i] >= 0:   
            l.append(A[i])
            i+=1
            
        if (sum(l) > maxi):
            a = l
            maxi = sum(l)


    return a


A = [ 0, 0, -1, 0 ]
A = [ 0, 0, 0, 0 ]
A = [ 1, 2, 5, -9, 2, 3]

print(maxset(A))