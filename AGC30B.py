L,N=map(int,input().split())
now=0
lists=[]
for i in range(N):
    lists.append(int(input()))
while lists:
    former_power=min(lists)-now
    latter_power=(now+L)-max(lists)
