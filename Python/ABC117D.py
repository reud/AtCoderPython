import collections

N, K = map(int, input().split())
As = input().split()
As = [int(As[i]) for i in range(N)]

kn = max(As)

if kn < K:
    K_bins = format(K, 'b')
else:
    K_bins = format(K, '0{}b'.format(len(format(kn, 'b'))))

As = [format(i, '0{}b'.format(len(K_bins))) for i in As]

ans = ''
ansum = 0
score = 0
for i in range(len(K_bins)):
    target = [s[i] for s in As]

    ones = target.count('1')
    zeros = len(target) - ones
    if ones < zeros and (ansum + 1 if i == (len(K_bins) - 1) else 2 ** i) <= K:


        ans += '1'
        ansum += (1 if i == (len(K_bins) - 1) else 2 ** (len(K_bins)-1-i))
        score += (1 if i == (len(K_bins) - 1) else 2 ** (len(K_bins)-1-i) )* zeros

    else:
        ans += '0'
        score += (1 if i == (len(K_bins) - 1) else 2 ** (len(K_bins)-1-i) ) * ones

print(score)
