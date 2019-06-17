N = int(input())
score = 0
box = []
if N % 2 == 1:
    N -= 1
    score += 1
    box.append(1)

while N > 1:
    N /= 2
    box.append(2)

print(len(box))
for i in box:
    print(i)
