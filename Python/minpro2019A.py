A, B = map(int, input().split())
avail= int(A/2) if int(A/2)==(A/2) else int(A/2)+1
print('YES' if B<=avail else 'NO')