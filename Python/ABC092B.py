N=int(input())
D,X=map(int,input().split())
A=[int(input()) for _ in range(N)]
chocolate=X
for a in A:
    y=0
    i=0
    while True:
        y=i*a+1
        if y<=D:
            chocolate+=1
        else:
            break
        i+=1
print(chocolate)