N, S, T = map(int, input().split())
W = int(input())
moves = []
for i in range(N-1):
    moves.append(int(input()))

score = 0

if S <= W <= T:
    score += 1

for i in moves:
    W += i
    if S <= W <= T:
        score += 1

print(score)
