avails = input().split()
for i in range(len(avails)):
    avails[i] = int(avails[i])

avails.sort()

print(avails[0] + avails[1])
