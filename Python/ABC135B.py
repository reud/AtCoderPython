N = int(input())
P = [int(i) for i in input().split()]
T = [ i for i in range(1,N+1)]

missc = 0
for i in range(N):
    if P[i]!=T[i]:
        missc+=1

print( 'YES' if missc==2 or missc==0 else 'NO')