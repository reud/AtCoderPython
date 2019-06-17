A, B = map(int, input().split())
if A == 1:
    A = 9999
if B == 1:
    B = 9999
print('Alice' if A > B else 'Draw' if A == B else 'Bob')
