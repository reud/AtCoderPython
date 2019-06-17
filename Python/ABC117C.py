N,M=map(int,input().split())
Xs=list(map(int,input().split()))


Xs.sort()
costs=[abs(Xs[i]-Xs[i+1]) for i in range(M-1)]
costs.sort(reverse=True)

for i in range(N-1):
    if not costs:
        print(0)
        exit(0)
    costs.pop(0)




print(sum(costs))