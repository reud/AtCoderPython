import collections
N=int(input())
S=[int(input()) for _ in range(N)]
M=int(input())
T=[int(input()) for _ in range(N)]

S_col=collections.Counter(S)
T_col=collections.Counter(T)
S_item=S_col.items()
T_item=T_col.items()

