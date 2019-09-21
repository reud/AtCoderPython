from scipy.special import comb

ans = 1
k = 18
while k:
    ans *= comb(k, 3)
    k -= 3
print(ans)
