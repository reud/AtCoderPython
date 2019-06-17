X, A, B = map(int, input().split())

if B - A <= 0:
    print('delicious')
elif X >= (B - A):
    print('safe')
else:
    print('dangerous')
