#https://www.interviewbit.com/problems/bulbs/
def bulbs(A):

    cnt = 0
    changed = False

    for x in A:
        if (not changed and x == 0) or (changed and x == 1):
            cnt += 1
            changed = not changed

    return cnt


A = [0, 1, 0, 1]
print(bulbs(A))