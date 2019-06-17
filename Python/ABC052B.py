N = int(input())
S = input()
max = 0
x = 0
for i in S:
    if i == 'I':
        x += 1
    else:
        x -= 1
    if max < x:
        max = x

print(max)
