N, T = map(int, input().split())
Timers = [int(i) for i in input().split()]
subTs = [0] * N
for t in range(1, N):
    subTs[t] = Timers[t] - Timers[t - 1]

score = T * N
time = T
for i in range(1, N):
    # お湯でている時にスイッチが押された場合
    if subTs[i] < time:
        lost = T - subTs[i]
        score -= lost
print(score)
