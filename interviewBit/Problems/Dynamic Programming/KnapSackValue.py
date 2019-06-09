

def knapSack(A, maxWeight):

    M = [[0 for x in range(maxWeight+1)] for x in range(len(A)+1)]
    W = maxWeight
    for i in range(0, len(A) + 1):
        for j in range(0, maxWeight + 1):
            if i == 0 or j == 0:
                M[i][j] = 0
            elif A[i]["w"] > j:
                M[i][j] = M[i - 1][j]
            else:
                M[i][j] = max(A[i]["v"] + M[i - 1][j - A[i]["w"]], M[i - 1][j])

    for i in range(0, len(A) + 1):
        for j in range(0, maxWeight + 1):
            print(M[i][j], end=' ')
        print("\n")

    return M[len(A)][maxWeight]

# opt(i, w) = max{vi + OPT(i-1, w-w(i)), OPT(i-1), w}


# main

from collections import defaultdict

items = defaultdict(list)

items[1] = {"w": 1, "v": 15}
items[2] = {"w": 5, "v": 10}
items[3] = {"w": 3, "v": 9}
items[4] = {"w": 4, "v": 5}


print("f max = f(n,M) = ", knapSack(items, 8))