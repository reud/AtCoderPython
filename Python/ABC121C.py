N, M = map(int, input().split())
shops = [[int(i) for i in input().split()] for _ in range(N)]
shops.sort(key=lambda x: x[0])

money = 0
need = M
for shop in shops:
    if shop[1] >= need:
        print(money + need * shop[0])
        exit(0)
    need -= shop[1]
    money += shop[0] * shop[1]
