from functools import cmp_to_key
def largestNumber(A):
    ''' When comparing numbers we must pick the one leading
        to the best concatenated result:
        787978 > 787879  so 7879 is 'bigger' than 78
                    but     7879 is 'less' than 788
    '''

    # Convert to string once, for proper comparison a+b vs b+a
    A = map(str, A)  # convert every element in A to a string

    # swap iff a+b >= b+a
    key = cmp_to_key(lambda a, b: 1 if a + b >= b + a else -1)
    res = ''.join(sorted(A, key=key, reverse=True))  # join returns concatenated string with the elements of the list
    # Must left trim 0, apparently
    res = res.lstrip('0')
    return res if res else '0'


def cmp_func(x, y):
    if int(str(x) + str(y)) > int(str(y) + str(x)):
        return 1
    elif int(str(x) + str(y)) < int(str(y) + str(x)):
        return -1
    return 0


def mykey_func(my_cmp):
    class Key:
        def __init__(self, obj, *args):
            self.obj = obj

        def __lt__(self, other):
            return my_cmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            return my_cmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            return my_cmp(self.obj, other.obj) == 0

        def __le__(self, other):
            return my_cmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return my_cmp(self.obj, other.obj) >= 0

        def __ne__(self, other):
            return my_cmp(self.obj, other.obj) != 0

    return Key

def largestNumberFAST(A):
    sorted_arr = list(reversed(sorted(A, key=mykey_func(cmp_func))))
    i = 0
    # remove 0 from the left side
    while sorted_arr[i] == 0 and i < len(A) - 1:
        i += 1
    return ''.join([str(x) for x in sorted_arr[i:]])

A = [ 3, 30, 34, 5, 9]


print(largestNumberFAST(A))


# example of using map
'''

numbers1 = [1, 2, 3] 
numbers2 = [4, 5, 6] 
  
result = map(lambda x, y: x + y, numbers1, numbers2) 

'''


