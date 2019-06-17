N=int(input())
A=input()
B=input()
C=input()

score=0
for i in range(N):
    chas=[]
    chas.append(A[i])
    chas.append(B[i])
    chas.append(C[i])
    lens=len(list(set(chas)))
    score+=(lens-1)

print(score)
