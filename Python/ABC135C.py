N = int(input())
A = [ int(i) for i in input().split()]
B = [int(i) for i in input().split()]

score=0
for n in range(N):
    if A[n]>=B[n]:
       score+=B[n]
    else:
        B[n]-=A[n]
        score+=A[n]
        if A[n+1]>=B[n]:
            A[n+1]-=B[n]
            score+=B[n]
        else:
            score+=A[n+1]
            A[n+1]=0

print(score)
