K, A, B = map(int, input().split())
# snuke can biscket add otr huyasu


bis = 1
ad = B - A
starts = 2
if (B - A) > 1:
    bis = A
    K -= (A - 1)
    if K <= 1:
        print(bis + 1)
        exit(0)
    mades = int(K / 2)
    if (K /2- mades) != 0:
        bis += 1
    bis += (mades * ad)
    print(bis)
    exit(0)
else:
    print(K + 1)
    exit(0)
