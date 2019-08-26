xy = {(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)}
A_MASS_COUNT = 12
B_MASS_COUNT = 16
C_MASS_COUNT = 11

H, W = map(int, input().split())

l = [list(input()) for _ in range(H)]

counter = [0, 0, 0]

for h in range(H):
    for w in range(W):
        if l[h][w] == 'o':
            l[h][w] = '.'
            tmp = {(h, w)}
            max_height = min_height = w
            count = 1
            while len(tmp):
                ch, cw = tmp.pop()
                for x, y in xy:
                    if l[x + ch][y + cw] == 'o':
                        l[x + ch][y + cw] = '.'
                        tmp.add((x + ch, y + cw))
                        max_height = max(y + cw, max_height)
                        min_height = min(y + cw, min_height)
                        count += 1
            # resize to 1x
            # print(f'{max_height} {min_height}')
            count //= max(((max_height - min_height + 1) // 5) ** 2,1)
            if A_MASS_COUNT == count:
                counter[0] += 1
            elif B_MASS_COUNT == count:
                counter[1] += 1
            elif C_MASS_COUNT == count:
                counter[2] += 1
            else:
                ArithmeticError()

print(' '.join([str(i) for i in counter]))
