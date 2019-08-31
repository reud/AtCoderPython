N = int(input())
l = [int(input()) for _ in range(N)]
dp = [0] * N
dp[0] = 1

for i in range(1, N):

    zouka = True
    for j in range(i):
        if l[j] > l[i]:
            dp[i] = dp[j - 1] + 1
            zouka = False
            break
    if zouka:
        dp[i] = dp[i - 1] + 1

print(N-max(dp))
