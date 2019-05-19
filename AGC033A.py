def dig(tag, end):
    h = tag[0]
    w = tag[1]
    delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    s = set()
    for d in delta:
        if not h + d[0] < 0 and not h + d[0] >= H and not w + d[1] < 0 and not w + d[1] >= W and tag not in end:
            s.add((h + d[0], w + d[1]))
    return s


H, W = map(int, input().split())
black_mass = set()

for h in range(H):
    line = input()
    for w in range(W):
        if line[w] == '#':
            black_mass.add((h, w))

count = -1
end = set()
targets = black_mass
next_que = set()
while True:
    count += 1
    next_que = set()
    for tag in targets:
        next_que = next_que | dig(tag, end)
        end.add(tag)
    # print('next que',next_que)
    # print('end:',end)
    targets = next_que
    if len(end) == H * W:
        print(count)
        exit(0)
