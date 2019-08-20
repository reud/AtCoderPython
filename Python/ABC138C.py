N = int(input())
Vs = [int(i) for i in input().split()]

Vs.sort()

for vi in range(1,len(Vs)):
    Vs[vi]=(Vs[vi]+Vs[vi-1])/2

print(Vs[-1])