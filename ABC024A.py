A, B, C, K = map(int, input().split())
S, T = map(int, input().split())

money = (S * A) + (T * B)

if (S + T) >= K:
    money -= (C * (S + T))

print(money)
