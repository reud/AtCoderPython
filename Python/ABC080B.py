N = input()

f = sum([int(i) for i in N])

if int(N) % f == 0:
    print('Yes')
else:
    print('No')
