N=int(input())
listA=[] #appendのために宣言が必要
for i in range(N):
    a,b,c=input().split()
    listA.append([int(a), int(b),int(c)])
cl=[]
h=[]
for ix in range(0,100):
    for iy in range(0,100):
        if( listA[c]-abs(listA[a]-ix)-abs(listA[b]-iy) ):
            cl.append((ix,iy))
for i in cl:
    for i2 in listA:
        if (listA[ c ] - abs ( listA[ a ] - ix ) - abs ( listA[ b ] - iy )):
