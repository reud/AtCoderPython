import math

S=int(input())
def trial_division(n):
    #素因数を格納するリスト
    factor = []
    #2から√n以下の数字で割っていく
    tmp = int(math.sqrt(n)) + 1
    for num in reversed(range(2, tmp)):
        while n % num == 0:
            n //= num
            factor.append(num)
            if len(factor)==3:
                return factor
    #リストが空ならそれは素数
    if not factor:
        return 'prime number'
    else:
        factor.append(n)
        return factor

cS=S//2

y1 = S
x3 = 1
if y1<10**9:
    print('0 {} 0 0 {} 0'.format(y1,x3))
    exit(0)

div = min(10**6,y1)

print(trial_division(S))

exit(0)

while True:
    if y1%div ==0:
        y1/=div
        x3*=div
        print('find {} {} {}'.format(div,y1,str(x3)))
        div = max(y1,10**6)
        if y1<10**9 and x3<10**9:
            print('0 {} 0 0 {} 0'.format(y1, x3))
            exit(0)
    else:
        div-=1

