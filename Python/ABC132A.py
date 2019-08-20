S = input()
for i in range(len(S)):
    if S.count(S[i]) != 2:
        print('No')
        exit(0)

print('Yes')
