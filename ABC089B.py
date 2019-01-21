N=int(input())
S=input().split()

S=list(set(S))

if len(S)==3:
    print('Three')
    exit(0)
else:
    print('Four')
    exit(0)