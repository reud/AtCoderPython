
# 入力
N, A, B, C = map(int, input().split())
L = [int(input()) for i in range(N)]

INF = 10 ** 9


def dfs(cursor, a, b, c):  # cursor:カーソル a,b,c:現在の竹の長さ
    if cursor == N:  # cursorが最後まで行ったら終了する。
        return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else INF
    # abs(a - A) + abs(b - B) + abs(c - C) - 30 でなぜ30を減じているのかというと、
    # dfs(0,0,0)
    # dfs(0,0,0,0)で始まる以上、最初に選ばれるa,b,cを決定する際にもコストが10増加してしまうからである。
    # また、全探索を行う中で、a,b,cの初期値が0,0,0である以上、a,b,cのどれかが0のまま終了する場合が存在する。
    # この場合はa,b,cに竹が対応してないと言えるため、解にはならない、そこで三項演算子を利用して
    # その場合についてコストをINFとしている

    # 以下は4**Nで展開される再起処理となる。
    # カーソルの当たっている竹に対して、(A or B or Cに合成する) or (合成しない)の場合に分ける
    no_compound_pattern = dfs(cursor+1, a, b, c)
    compound_a_pattern = dfs(cursor+1, a + L[cursor], b, c)+10
    compound_b_pattern = dfs(cursor+1, a, b + L[cursor], c)+10
    compound_c_pattern = dfs(cursor+1, a, b, c + L[cursor])+10

    # 結果的に以下の値が返るのはそれぞれのパターンのコストが決定されてからなので
    # 以下のコードは最終的なコストの最小値
    return min(no_compound_pattern, compound_a_pattern, compound_b_pattern, compound_c_pattern)


print(dfs(0, 0, 0, 0))
