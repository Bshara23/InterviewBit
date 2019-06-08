#https://www.interviewbit.com/problems/assign-mice-to-holes/

def mice(A, B):

    A.sort()
    B.sort()
    i = j = 0
    lenA = len(A)
    maxx = 0
    while i < lenA:
        dist = abs(A[i] - B[i])
        maxx = dist if dist > maxx else maxx
        i += 1
        j += 1


    return maxx







A = [4, -4, 2]
B = [4, 0, 5]
print(mice(A, B))