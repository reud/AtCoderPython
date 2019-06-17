s = input()
t = input()
slist = []
tlist = []
for i in s:
    slist.append(ord(i))
for i in t:
    tlist.append(ord(i))

slist.sort()
tlist.sort(reverse=True)

while True:
    if not slist and not tlist:
        print('No')
        exit(0)
    elif not tlist:
        print('No')
        exit(0)
    elif not slist:
        print('Yes')
        exit(0)

    spop = slist.pop(0)
    tpop = tlist.pop(0)

    if spop == tpop:
        pass
    elif spop > tpop:
        print('No')
        exit(0)
    else:
        print('Yes')
        exit(0)
