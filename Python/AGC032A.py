N = int(input())
B = input().split()

history = []
while len(B):

    if B[0] != '1':
        print(-1)
        exit(0)

    bef_kick_len = len(B)
    # if failed, go to kill original

    for ind in range(len(B))[::-1]:
        # print("index {} value {}".format(ind+1, B[ind]))
        if int(B[ind]) == ind + 1:
            history.append(B.pop(ind))
            break

    if len(B) == bef_kick_len:
        for state in range(len(B) - 1):
            # print("state {} state+1 {}".format(state,B[state]))
            if B[state] == B[state + 1]:
                history.append(B.pop(state))
                break

# print(history)

rev_his = reversed(history)
for i in rev_his:
    print(i)
