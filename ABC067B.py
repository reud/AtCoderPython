N, K = map(int, input().split())
L = [int(l) for l in input().split()]
L.sort(reverse=True)
ans = 0
for i in range(K):
    ans += L[i]

print(ans)
