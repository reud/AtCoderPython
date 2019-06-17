N,M=map(int,input().split())
lmax=0
rmin=9999999
for i in range(M):
    l,r=map(int,input().split())
    lmax=max(lmax,l)
    rmin=min(rmin,r)

print(max(rmin-lmax+1,0))
