


def diffPossible(A, B):

    lenA = len(A)
    D = {}
    for i in range(lenA):
        D[A[i]] = i

    for i in range(lenA):
        if D.__contains__(A[i] - B) and D[A[i] - B] != i:
            return True

    return False

def otherSolution(A, B):
    mapp = {}
    for x in A:
        """
        dict.get(key[, default]) → value
        Get the item with the given key, similar to dict[key]. If the key is not present and default 
        is given, supply default instead. 
        If the key is not present and no default is given, raise the KeyError exception.
        """
        # look for either x+B or x-B, this way we can check and then add, no need to pass
        # over the array twice, return False if x+B or x-B not found
        if mapp.get(x + B, False) == True or mapp.get(x - B, False) == True:
            return 1
        mapp[x] = True # set the value of x to true, thus when its found we get True and when its not found we get False
        
    return 0

A = [0]
print(otherSolution(A, 0))

"""
Mappings and Dictionaries
http://buildingskills.itmaybeahack.com/book/python-2.6/html/p02/p02c05_maps.html
"""