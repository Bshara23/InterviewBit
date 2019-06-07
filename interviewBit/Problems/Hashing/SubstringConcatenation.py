
def validSegment(A, B, lenB, SaveGame):
    D = {}
    for x in B:
        D[x] = 0

    for i in range(0, len(A), lenB):
        if D.get(A[i: i + lenB], -1) >= 0:
            D[A[i: i + lenB]] += 1
        elif D.get(A[i: i + lenB], False) == False:
            return False


    for k in D.keys():
        if SaveGame[k] != D[k]:
            return False

    return True

def findSubstring(A, B):



    if len(B) == 0 or len(A) == 0:
        return []
    segsize = len(B) * len(B[0])
    if segsize > len(A):
        return []

    SaveGame = {}
    for x in B:
        if SaveGame.get(x, False) == False:
            SaveGame[x] = 1
        elif SaveGame.get(x, False) >= 0:
            SaveGame[x] += 1


    res = []
    for i in range(len(A) - segsize + 1):

        if validSegment(A[i:i+segsize], B, len(B[0]), SaveGame):
            res.append(i)
            #i += segsize
    return res



A = "barfoothefoobarman"
B = [ "foo", "bar" ]
print(findSubstring(A, B))

D = {}
