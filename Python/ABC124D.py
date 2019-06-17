N, K = map(int, input().split())
S = input()
isStartZero = True if S[0] == '0' else False
# zli = [x for x in S.split('1') if x]
zli = [x for x in S.split('1') if x == '0' or x]
oli = [x for x in S.split('0') if x]
li = list(sum(zip(zli, oli) if isStartZero else zip(oli, zli), ()))
if len(zli) > len(oli):
    li.append(zli[-1])
elif len(oli) > len(zli):
    li.append(oli[-1])

sumli = []
for t in range(K):
    if len(li) > 2:
        print(li)
        sumli = []
        for i in range(1, len(li) - 1):
            sumli.append(len(str(li[i - 1])) + len(str(li[i])) + len(str(li[i + 1])))
        key = -1
        sortedsumli = sorted(sumli, reverse=True)
        e = True
        mi = -1
        while e:
            for m in sortedsumli:
                cind = sumli.index(m)
                if cind % 2 == 0 and (not isStartZero):
                    key = cind
                    e = False
                    mi = m
                    print('mi:{}'.format(mi))
                    if t == (K - 1):
                        print(mi)
                        exit(0)
                    li.pop(key)
                    li.pop(key)
                    li.pop(key)
                    li.insert(key, '1'*mi)
                    break
                elif cind % 2 == 1 and isStartZero:
                    key = cind
                    e = False
                    mi = m
                    print('mi:{}'.format(mi))
                    if t == (K - 1):
                        print(mi)
                        exit(0)
                    li.pop(key)
                    li.pop(key)
                    li.pop(key)
                    li.insert(key, '0'*mi)
                    break



