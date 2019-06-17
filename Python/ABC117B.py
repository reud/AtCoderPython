input()
L=input().split()

for i in range(len(L)):
    L[i]=int(L[i])



print('Yes' if max(L)<(sum(L)-max(L)) else 'No')