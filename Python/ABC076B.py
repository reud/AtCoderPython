keizi = 1
N = int(input())
K = int(input())

for _ in range(N):
    Adis = keizi
    Bdis = K
    if Adis < Bdis:
        keizi *= 2
    else:
        keizi += K

print(keizi)
