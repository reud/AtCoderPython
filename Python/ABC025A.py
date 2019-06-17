yobina=[]
S=input()
N=int(input())

for f in S:
    for l in S:
        yobina.append('{}{}'.format(f,l))

print(yobina[N-1])