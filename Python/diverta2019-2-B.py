
import itertools


def linerFunc(targetX, targetY, Xa, Ya, Xb, Yb):
    # print(f'{targetX} {targetY} {Xa} {Ya} {Xb} {Yb}')
    if Xb-Xa ==0:
        return False
    alpha = (Yb - Ya)/(Xb - Xa)
    beta = Yb - alpha * Xb
    val = float(alpha*targetX+beta)
    return True if val == targetY else False

def is_on(f,x,y):
    if f(x)==y:
        return True
    else:
        return False

N=int(input())
points=[]
for i in range(N):
    x,y = map(int,input().split())
    points.append((x,y))

funcs=[]
combs = list(itertools.combinations(points,2))


res=[]
for c in combs:
    count=0
    for p in points:
        if linerFunc(p[0],p[1],c[0][0],c[0][1],c[1][0],c[1][1]):
            count+=1
    res.append(count)
# print(N-max(res))
print(max(N-max(res),1))