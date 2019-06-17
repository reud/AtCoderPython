A,B,C=map(int,input().split())
score=0
gedoku=A+B

if(C>(gedoku+1)):
    score=B+gedoku+1
else:
    score=B+C
print(score)