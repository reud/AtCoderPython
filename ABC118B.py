N, M = map(int, input().split())
likes = [[int(i) for i in input().split()] for _ in range(N)]
seki = {}
for i in range(N):
    if seki == {}:
        seki = {likes[i][j] for j in range(1, likes[i][0]+1)}

    tag={likes[i][j] for j in range(1, likes[i][0]+1)}
    seki= seki & tag

print(len(seki))