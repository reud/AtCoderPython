A, B, K = map(int, input().split())
r = max(A, B)
q = []
for i in range(1, r + 1):
    if A % i == 0 and B % i == 0:
        q.append(i)

q.sort(reverse=True)

print(q[K-1])
