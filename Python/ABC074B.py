N=int(input())
K=int(input())
X=[int(x) for x in input().split()]

distance=0
for i in X:
    adis=i*2
    bdis=abs(K-i)*2
    if adis<bdis:
        distance+=adis
    else:
        distance+=bdis
print(distance)