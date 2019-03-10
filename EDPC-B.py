N,K=map(int,input().split())
H=[0]+[int(h) for h in input().split()]
dp = [999999999 for _ in range(N + 1)]
dp[0] = 0
dp[1] = 0
dp[2] = abs(H[2] - H[1])
for i in range(3, N + 1):
    if i-K < 1:
        starter=1
    else:
        starter=i-K

    lists=[dp[i]]+[dp[x]+abs(H[x]-H[i]) for x in range(starter,i)]

    dp[i] = min(lists)


print(dp[N])

