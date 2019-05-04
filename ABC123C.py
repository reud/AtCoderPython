import math
N=int(input())
TOSHI=[int(input()) for _ in range(5)]
COST=math.ceil(N/min(TOSHI))
print(4+COST)