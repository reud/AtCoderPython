def parse_ans(answer):
    return answer % ((10 ** 9) + 7)


def get_sigma(a, d):
    n = K
    #print('しょこう {} 公差 {}'.format(a,d))
    return (1 / 2) * n * (2 * a + (n - 1) * d)


N, K = map(int, input().split())
As = [int(i) for i in input().split()]

# K=1で取られたマウントの数(初項) <- Bi>BjならBjはマウントを取られた index -> 場所
mounted = [0] * len(As)
# 自分より強い値　(公差)　index -> 場所
more_strong = [0] * len(As)

# 強いランキング
tuyosa_banduke = sorted(As, reverse=True)

for i in range(len(As)):
    tuyosa_rank = tuyosa_banduke.index(As[i])  # 0 -> 最強
    more_strong[i] = tuyosa_rank
    for j in range(i + 1, len(As)):
        if As[i] > As[j]:
            mounted[j] += 1

print([get_sigma(mounted[i], more_strong[i]) for i in range(len(As))])
print(parse_ans(sum([get_sigma(mounted[i], more_strong[i]) for i in range(len(As))])))
