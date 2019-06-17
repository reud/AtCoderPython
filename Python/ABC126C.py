import math
N,K=map(int,input().split())

sum=0
for deme in range(1,N+1):
    need_challenge=max(0,math.ceil(math.log2(K)-math.log2(deme)))
    sum+=float((1/N)*((1/2)**need_challenge))
print('{:.13f}'.format(sum))