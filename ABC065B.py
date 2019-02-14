N = int(input())
A = [0]  # parser
A += [int(input()) for i in range(N)]
count = 1
flashed = A[1]
if flashed==2:
    print(1)
    exit(0)
while True:
    flashed = A[flashed]
    count += 1
    if flashed == 2:
        print(count)
        exit(0)
    elif count > 10 ** 6:
        print(-1)
        exit(0)
