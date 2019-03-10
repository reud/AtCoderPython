N, M, C = map(int, input().split())
bias = [int(i) for i in input().split()]
sources = [[int(i) for i in input().split()] for _ in range(N)]

oks = 0

for source in sources:
    score = C
    for key in range(M):
        score += bias[key] * source[key]
    if score> 0:
        oks += 1

print(oks)
