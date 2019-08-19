N, M = map(int, input().split())
bites = [(int(i[0]), int(i[1])) for i in input().split()]
dp = [0]
dp.extend([0 for _ in range(N)])
for i in range(1,N+1):
    dp[i]=min(dp[i],dp[i-1])
    print(i)
