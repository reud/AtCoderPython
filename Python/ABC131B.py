N,L=map(int,input().split())
ringos = [ L+i-1 for i in range(1,N+1)]

abs_ringos=[abs(i) for i in ringos]

min_key=0
amin_ringo=99999
for i in range(len(abs_ringos)):
    if amin_ringo != min(amin_ringo,abs_ringos[i]):
        amin_ringo = abs_ringos[i]
        min_key=i

print(sum(ringos)-ringos[min_key])