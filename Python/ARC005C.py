import sys

sys.setrecursionlimit(10 ** 6)
used = [[-1] * 502 for _ in range(502)]
dxy = ((0, -1), (1, 0), (-1, 0), (0, 1))
MAP = []
H = W = 0


def dfs(h, w, k):

    if MAP[h][w] == 's' or MAP[h][w] == '.':
        used[h][w] = k
    elif MAP[h][w] == '#':
        if k < 2:
            k += 1
            used[h][w] = k
        else:
            used[h][w] = k
            return
    elif MAP[h][w] == 'g':
        print('YES')
        exit(0)
        return
    else:
        used[h][w] = k
        return

    for x, y in dxy:
        if used[h + x][w + y] != -1 and (used[h + x][w + y] <= k):
            continue
        dfs(h + x, w + y, k)

    return


def main():
    H, W = map(int, input().split())
    MAP.append(['x' for _ in range(W + 2)])

    st = (9999, 9999)
    for s in range(H):
        l = input()
        l = 'x' + l + 'x'
        if 's' in l:
            st = (s + 1, list(l).index('s'))
        MAP.append(list(l))
    MAP.append(['x' for _ in range(W + 2)])

    x, y = st
    dfs(x, y, 0)
    print('NO')
    exit(0)

if __name__ == "__main__":
    main()
