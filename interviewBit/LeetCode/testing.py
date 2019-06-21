
a = "101"



def binrepinv(str):
    res = ""
    for i in str:
        if i == '1':
            res += '0'
        else:
            res += '1'
    return res

res = {}
res["101"] = 1
res["010"] = 1
res["111"] = 3
res["000"] = 3

etto = True
for i in res:
    if binrepinv(i) in res:
        if res[binrepinv(i)] != res[i]:
            etto = False
    else:
        etto = False
        break

print(etto)
