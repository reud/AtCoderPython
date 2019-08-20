N=int(input())

Hs=[int(i) for i in input().split()]
Hs.append(10**9+3)
same = False

for i in range(N):
    fp=i+1
    p=i
    if Hs[p]<=Hs[fp]:
        same=False
        if Hs[p]==Hs[fp]:
            same=True
        continue
    else:
        if same:
            print('No')
            exit(0)
        if (Hs[p])<=(Hs[fp]-1):
            if Hs[p]==Hs[fp]-1:
                same=True
            continue
        else:
            print('No')
            exit(0)
print('Yes')





