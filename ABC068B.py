N = int(input())
ans = [2 ** i for i in range(0, 7)]

for i in range(len(ans)):
    if ans[i] > N:
        print(ans[i-1])
        exit(0)
print(64)
