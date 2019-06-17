N = int(input())
s = input()

red = 0
blue = 0
for i in s:
    if i == 'R':
        red += 1
    else:
        blue += 1

print('Yes' if red > blue else 'No')
