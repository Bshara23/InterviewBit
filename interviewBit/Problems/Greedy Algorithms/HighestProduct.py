#https://www.interviewbit.com/problems/highest-product/
# did not understand the question...

def maxp3(A):
    n = len(A)

    max1 = max(A)
    A.remove(max1)
    max2 = max(A)
    A.remove(max2)
    max3 = max(A)

    A.append(max1)
    A.append(max2)

    min1 = min(A)
    A.remove(min1)
    min2 = min(A)

    product = max(max1 * max2 * max3, max1 * min1 * min2)

    return product