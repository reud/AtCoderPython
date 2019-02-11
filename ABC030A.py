A, B, C, D = map(int, input().split())
print('TAKAHASHI' if (B / A) > (D / C) else 'DRAW' if (B / A) == (D / C) else 'AOKI')
