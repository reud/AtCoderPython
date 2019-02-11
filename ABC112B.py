N,T=map(int,input().split())

listA=[] #appendのために宣言が必要
for i in range(N):
    a,b=input().split()
    listA.append([int(a), int(b)])

for i in range(len(listA)):
    if(T<listA[i][1]):
        listA[i][0]=9999

minc=9999
index=9999
for i in range(len(listA)):
    if(minc>listA[i][0]):
        minc=listA[i][0]
        index=i
if(minc==9999):
    print('TLE')
    exit(0)
print(minc)

