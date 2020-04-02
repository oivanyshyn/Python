from collections import defaultdict
kv = defaultdict(str)
access = []
maxSize = 4

def cacheSet(key, value):
    kv[key] = value
    if key in access:
        access.remove(key)
        access.append(key)
    else:
        access.append(key)
    if len(access) > maxSize:
        access.pop(0)

def cacheGet(key):
    if key in kv:
        access.remove(key)
        access.append(key)
        return kv[key]
    else:
        return None
def cachePrint():
    for k,v in kv.items():
        print(k,v)


for i in range(4):
    cacheSet(i, "value " + str(i+1))
for i in range(4):
    print(cacheGet(i))
    cacheSet(0, "value " + str(5))
    cacheSet(1, "value " + str(6))
cachePrint()