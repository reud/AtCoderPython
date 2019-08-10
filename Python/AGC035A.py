N = int(input())
a = [int(i) for i in input().split()]
all_xor = a[0]

for ai in range(len(a) - 1):
    all_xor = all_xor ^ a[ai + 1]

for ai in a:
    if ai ^ all_xor != ai:
        print('No')
        exit(0)

print('Yes')
exit(0)
