n = int(input())
Ps = [int(n) for n in input().split()]
score=0
for ind in range(len(Ps)-2):
    p1 = Ps[ind]
    p2 = Ps[ind+1]
    p3 = Ps[ind+2]
    l = [p1,p2,p3]
    if max(l)!=p2 and min(l)!=p2:
       score+=1
print(score)
