# 解答ちらっと見た
# 問題のキモは Cx,Cy,Hがそれぞれ100通り、
# 全探索をCx,Cy,Hに対して試みると 入力された情報のcheckを入れて101*101*100*100でTLEする。
# でもよく考えてみると、Cx,CyがわかればHはそのあとで出せるので Cx,Cyに対して全探索をする(101*101*Nの計算量で済む)


def get_H(Cx, Cy):
    for x, y, h in L:
        if h > 0:
            return abs(x - Cx) + abs(y - Cy) + h


def check_H(Cx, Cy, H):
    for x, y, h in L:
        if h != max(H - abs(x - Cx) - abs(y - Cy), 0):
            return False
    return True


N = int(input())

L = [(list(map(int, input().split()))) for _ in range(N)]

for Cx in range(101):
    for Cy in range(101):
        H = get_H(Cx, Cy)
        if check_H(Cx, Cy, H):
            print('{} {} {}'.format(Cx, Cy, H))
            exit(0)
