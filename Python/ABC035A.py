import fractions

W, H = map(int, input().split())
if int(W / fractions.gcd(W, H)) == 4:
    print('4:3')
else:
    print('16:9')

