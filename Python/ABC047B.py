W,H,N=map(int,input().split())
points=[[int(i) for i in input().split()] for _ in range(N)]

space=[[0 for _ in range(H)] for __ in range(W)]
for point in points:
    if point[2]==1:
        for i in range(W):
            for j in range(H):
                if i<point[0]:
                    space[i][j]=1
    elif point[2]==2:
        for i in range(W):
            for j in range(H):
                if i>=point[0]:
                    space[i][j]=1
    elif point[2]==3:
        for i in range(W):
            for j in range(H):
                if j<point[1]:
                    space[i][j]=1
    elif point[2]==4:
        for i in range(W):
            for j in range(H):
                if j>=point[1]:
                    space[i][j]=1

count=0

for i in range(W):
    for j in range(H):
        if space[i][j]==0:
            count+=1
print(count)