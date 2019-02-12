N = int(input())
A = [int(x) for x in input().split()]
count = 0
while True:
    for i in range(len(A)):
        if A[i] % 2 == 1:
            print(count)
            exit(0)
        A[i] /= 2
    count += 1
