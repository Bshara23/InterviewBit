

def f(A):

    if len(A) == 0:
        return 0
    dic = {}
    for x in A:
        if dic.get(x, False) == False:
            dic[x] = 1
        else:
            dic[x] += 1

    maxx = 0
    key = -1
    for k, v in dic.items():
        if maxx < v:
            maxx = v
            key = k

    return key

A = [100]

print(f(A))