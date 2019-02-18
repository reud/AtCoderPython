N=int(input())
T=[0]+[int(i) for i in input().split()]
M=int(input())
drinks=[[int(i) for i in input().split()] for _ in range(M)]
for drink in drinks:
    copyedT=[i for i in T]
    copyedT[drink[0]]=drink[1]
    print(sum(copyedT))