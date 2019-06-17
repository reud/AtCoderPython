A, B, C = map(int, input().split())
opened = []
x = 1
while True:

    if (A * x) % B == C:
        print('YES')
        exit(0)
    else:
        if (A * x) % B in opened:
            print('NO')
            exit(0)
        opened.append((A * x) % B)
        x += 1
