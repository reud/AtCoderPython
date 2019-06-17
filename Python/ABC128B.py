N = int(input())
sp = []
for i in range(N):
    S, P = input().split()
    P = int(P)
    sp.append([S, P, i + 1])

sp.sort(key=lambda x: x[1],reverse=True)
sp.sort(key=lambda x: x[0])
for i in sp:
    print(i[2])
