ans = [5, 5, 7]
haiku = [int(i) for i in input().split()]

haiku.sort()

if ans == haiku:
    print('YES')
else:
    print('NO')
