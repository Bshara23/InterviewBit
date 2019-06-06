#https://www.interviewbit.com/problems/equal-average-partition/
import itertools

def getSets(A):
    lenA = len(A)
    setT = []
    for i in range(1, lenA):
        setT.append(list(map(set, itertools.combinations(A, i))))

    length = 0
    for i in range(len(setT)):
        length += len(setT[i])
    print(length)

    return setT


#def avgset(A):


A = [1, 2, 3]
print(getSets(A))