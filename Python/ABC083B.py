n, a, b = map(int, input().split())
sum = 0
for i in range(0, n + 1):
    nlist = list(str(i))
    bflag = False
    keta_sum = 0
    for i2 in nlist:
        keta_sum += int(i2)
    if (a <= keta_sum and b >= keta_sum):
        sum += i
print(sum)
