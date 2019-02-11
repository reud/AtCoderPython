check = []
for i in range(3):
    check.append([int(input()), i, 0])

check.sort(key=lambda x: x[0],reverse=True)

for i in range(3):
    check[i][2] = i + 1

check.sort(key=lambda x: x[1])

for i in range(3):
    print(check[i][2])
