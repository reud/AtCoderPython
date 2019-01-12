N=int(input())
T,A=map(int,input().split())
H=input().split()
for i in range(len(H)):
    H[i]=int(H[i])
minimum=0
for i in range(len(H)):
    H[i]=abs(T-(H[i]*0.006)-A)
    if(H[minimum]>H[i]):
        minimum=i
print(minimum+1)
