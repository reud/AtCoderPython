N, M = map(int, input().split())

last_bin = (2 ** N)
switches = [[int(i) for i in input().split()][1:] for _ in range(M)]
ps = [int(i) for i in input().split()]

# print('{:010b}'.format(last_bin))

counter = 0
score = 0
while last_bin != counter:
    state = '{:010b}'.format(counter)
    # print(state)
    okFlag = True
    for i in range(len(switches)):
        # print(switches[i])
        states = [state[-1 * x] for x in switches[i]]
        # print(states)
        if states.count('1') % 2 == ps[i]:
            pass
        else:
            okFlag = False
            break
    if okFlag:
        score += 1
    counter += 1

print(score)