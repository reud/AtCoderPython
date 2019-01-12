import sys

sys.setrecursionlimit(10**6)

def sig(x):
    return 1 if x==1 else sig(x-1)+x


a,b=map(int,input().split())

upper=int(sig(b-a))
print(upper-b)


