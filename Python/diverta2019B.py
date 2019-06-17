R, G, B, N = map(int, input().split())

score = 0

for g in range(3001):
    for b in range(3001):
        if g + b > 3000:
            break
        if (N - (g * G + b * B)) >= 0 and (N - (g * G + b * B)) % R == 0:
            score += 1

print(score)