score = 0
for i in range(3):
    s, e = map(int, input().split())
    wari = e / 10
    score += s * wari

print(int(score))
