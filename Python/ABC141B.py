S=input()

for i in range(len(S)):
    ind = i+1
    if ind%2==1:
        if S[i]=='L':
            print('No')
            exit(0)
    else:
        if S[i]=='R':
            print('No')
            exit(0)
print('Yes')