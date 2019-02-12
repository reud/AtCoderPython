A, B = map(int, input().split())
S = input()

nums = [str(i) for i in range(10)]

if (A + B + 1) != len(S):
    print('No')
    exit(0)

for i in range(len(S)):
    if i == A:
        if S[i] != '-':
            print('No')
            exit(0)
    else:
        if not S[i] in nums:
            print('No')
            exit(0)

print('Yes')
