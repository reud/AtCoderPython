N = int(input())
lef_only_ex = False
rig_only_ex = False
lef_only_ex_hold = False
rig_only_ex_hold = False
back_a = 0
forward_b = 0
inside = 0
for i in range(N):
    lef_only_ex = False
    rig_only_ex = False
    line = input()
    if line[-1] == 'A':
        back_a += 1
        rig_only_ex = True
    if line[0] == 'B':
        forward_b += 1
        lef_only_ex = True
    if line[0] == 'B' and line[-1] == 'A':
        lef_only_ex = False
        rig_only_ex = False
    if lef_only_ex and not lef_only_ex_hold:
        lef_only_ex_hold = True
    if rig_only_ex and not rig_only_ex_hold:
        rig_only_ex_hold = True

    for s in range(len(line) - 1):
        if line[s] == 'A' and line[s + 1] == 'B':
            inside += 1
print((min(back_a, forward_b) - 1 if not lef_only_ex_hold and not rig_only_ex_hold else min(
    back_a, forward_b)) + inside)
