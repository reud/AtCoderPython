N = int(input())
S = [input() for _ in range(N)]
M = int(input())
T = [input() for _ in range(M)]
scorelists = []
for key in S:
    score = 0
    for tmp in S:
        if key == tmp:
            score += 1
    for tmp in T:
        if key == tmp:
            score -= 1
    scorelists.append(score)

print(max(scorelists) if max(scorelists) > 0 else 0)
