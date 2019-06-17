N = int(input())
H = [0] + [int(h) for h in input().split()]
dp = [999999999 for _ in range(N + 1)]
dp[0] = 0
dp[1] = 0
dp[2] = abs(H[2] - H[1])
for i in range(3, N + 1):
    dp[i] = min(dp[i], dp[i - 1] + abs(H[i - 1] - H[i]), dp[i - 2] + abs(H[i - 2] - H[i]))

print(dp[N])
