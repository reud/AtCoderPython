import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, Q = map(int, input().split())
connections = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    pa, ki = map(int, input().split())
    connections[pa].append(ki)
    connections[ki].append(pa)

scores = [0 for _ in range(N + 1)]
for _ in range(Q):
    tag, p = map(int, input().split())
    scores[tag] += p

i = 1

def dfs(k=1,bef=-1):
    global scores
    global fins
    kids = connections[k]
    if len(kids)==1 and bef==kids[0]:
        return
    for kid in kids:
        # print(f'k:{k} kids:{kids}')
        if bef==kid:
            continue
        scores[kid]+=scores[k]
        dfs(kid,k)


dfs()



print(*scores[1:])