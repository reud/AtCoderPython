import time

start = time.time()

H,W=map(int,input().split())

S=[input() for _ in range(H)]
used=[[0 for _ in range(W)] for _ in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j]=='#':
            if i-1>=0:



elapsed_time = time.time() - start
print(elapsed_time)

