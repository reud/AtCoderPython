N=int(input())
A = [int(input()) for _ in range(N)]

max1 = max(A)
max2 = sorted(A)[-2]

for a in A:
    print( max1 if max1 != a else max2)
