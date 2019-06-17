from itertools import chain
N,M=map(int,input().split())
roads=[list(map(int,input().split())) for _ in range(M)]
roads=list(chain.from_iterable(roads))
for i in range(1,N+1):
    print(roads.count(i))
