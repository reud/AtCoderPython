N=int(input())
W=[]
for i in range(N):
    A,B=map(int,input().split())
    W.append((A+B,A,B))
W.sort(key= lambda x:x[0],reverse=True)

isTakahashiTurn=True
score=0
for i in range(N):
    if isTakahashiTurn:
        score+=W[i][1]
        isTakahashiTurn=False
    else:
        score-=W[i][2]
        isTakahashiTurn=True
print(score)

