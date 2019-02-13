N = int(input())
score = 0
for _ in range(N):
    l, r = map(int, input().split())
    score += (r - l + 1)
print(score)
