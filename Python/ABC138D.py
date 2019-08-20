import sys


# 配列にアクセスする際 N-1 とかしたくないのでいくつかの配列で余分に大きさを持っている
sys.setrecursionlimit(10**6) # 一応
input = sys.stdin.readline # ないと死ぬ

### グラフの作成(親子関係なしの無向グラフ)
N, Q = map(int, input().split())
connections = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    connections[a].append(b)
    connections[b].append(a)
###

### Scoreの初期化( 今書くなら[0]*N+1 でよい)
scores = [0 for _ in range(N + 1)]
### それへのScore代入
for _ in range(Q):
    tag, p = map(int, input().split())
    scores[tag] += p

i = 1

# k -> 訪問先 bef -> 前回の訪問先
def dfs(k=1,bef=-1):
    global scores
    global fins
    kids = connections[k]
    # グラフの端っこかつ唯一の接続先が前回の訪問先なら終了
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