import collections
from functools import reduce
from operator import mul

N = int(input())
Hs = []


def cmb(n, r):
    try:
        r = min(n - r, r)
        if r == 0: return 1
        over = reduce(mul, range(n, n - r, -1))
        under = reduce(mul, range(1, r + 1))
        return over // under
    except:
        return 0


for line in range(N):
    l = list(input())
    l.sort()
    Hs.append(','.join(l).replace(',', ''))

c = collections.Counter(Hs)

su = 0
for v in c.values():
    su += cmb(v, 2)

print(su)
