N, Y = map(int, input().split())
a = 0
b = 0
c = 0
exist = False


def getSum():
    return 10001 * a + 5001 * b + 1001 * c


for fa in range(2001):
    if fa > N:
        print('-1 -1 -1')
        exit(0)
    for fb in range(2001):
        if fb > N:
            break
        elif N - fa - fb < 0:
            break
        if (fa * 9000 + fb * 4000 == (Y - 1000 * N)):
            a = fa
            b = fb
            c = N - fa - fb
            print('{} {} {}'.format(a, b, c))
            exit(0)

print('-1 -1 -1')
