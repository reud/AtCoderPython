H, W = map(int, input().split())
MAPS = [[i for i in input()]  for _ in range(H)]

for map in MAPS:
    print('w'.join(map).replace('w',''))
    print('w'.join(map).replace('w',''))
