n = int(input())
ans = n + 1
for i in range(1, n + 1):
    if i * i > n:
        break
    ans = min(ans, abs(n // i - i) + n % i)
print(ans)
