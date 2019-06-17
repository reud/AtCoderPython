H, W = map(int, input().split())
map = [list('.' * (W + 2)) for _ in range(H + 2)]
Smap = [input() for _ in range(H)]

# mapping

for line in range(1, H + 1):
    for row in range(1, W + 1):
        mapper = Smap[line - 1][row - 1]
        map[line][row] = mapper

for line in range(1, H + 1):
    for row in range(1, W + 1):

        bomb_counter = 0
        for counter_line in range(-1, 2):
            for counter_row in range(-1, 2):
                if counter_line == 0 and counter_row == 0:
                    pass
                elif map[counter_line + line][counter_row + row] == '#':
                    bomb_counter += 1
        if map[line][row] != '#':
            map[line][row] = str(bomb_counter)

for i in range(1, len(map)):
    print('.'.join(map[i]).replace('.', ''))
