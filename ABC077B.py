lists = [i * i for i in range(4 * (10 ** 4))]
N = int(input())

back_state = 1
for i in lists:
    if i - N > 0:
        print(back_state)
        exit(0)
    back_state = i
