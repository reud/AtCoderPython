import itertools
N=int(input())
S=[input() for _ in range(N)]
M=0
A=0
R=0
C=0
H=0
alives=0
march=['M','A','R','C','H']
for i in S:
    if i.startswith('M'):
        M+=1
    elif i.startswith('A'):
        A+=1
    elif i.startswith('R'):
        R+=1
    elif i.startswith('C'):
        C+=1
    elif i.startswith('H'):
        H+=1

if M==0:
    march.pop(march.index('M'))
if A==0:
    march.pop(march.index('A'))
if R==0:
    march.pop(march.index('R'))
if C==0:
    march.pop(march.index('C'))
if H==0:
    march.pop(march.index('H'))

if len(march)<3:
    print(0)
    exit(0)

seq=list(itertools.combinations(march,3))

ans=0
for i in seq:
    temp=1
    for ch in i:
        if ch=='M':
            temp*=M
        if ch=='A':
            temp*=A
        if ch=='R':
            temp*=R
        if ch=='C':
            temp*=C
        if ch=='H':
            temp*=H
    ans+=temp

print(ans)