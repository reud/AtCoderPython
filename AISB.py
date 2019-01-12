N = int(input())
A, B = map(int, input().split())
P = input().split()

low = []
middle = []
high = []

for i in range(len(P)):
    P[i] = int(P[i])
    if P[i] <= A:
        low.append(P[i])
    elif P[i] <= B:
        middle.append(P[i])
    else:
        high.append(P[i])

atta = [len(low), len(middle), len(high)]

print(min(atta))
