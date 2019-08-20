N=int(input())
score=0
for n in range(1,N+1):
    if len(str(n))%2==1:
       score+=1
print(score)