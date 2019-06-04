from functools import cmp_to_key
def largestNumber(A):
    ''' When comparing numbers we must pick the one leading
        to the best concatenated result:
        787978 > 787879  so 7879 is 'bigger' than 78
                    but     7879 is 'less' than 788
    '''

    # Convert to string once, for proper comparison a+b vs b+a
    A = map(str, A)
    key = cmp_to_key(lambda a, b: 1 if a + b >= b + a else -1)
    res = ''.join(sorted(A, key=key, reverse=True))
    # Must left trim 0, apparently
    res = res.lstrip('0')
    return res if res else '0'




A = [ 3, 30, 34, 5, 9]


print(largestNumber(A))
