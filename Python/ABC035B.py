S = input()
T = int(input())
UpperSub = abs(S.count('L') - S.count('R'))
DownerSub = abs(S.count('U') - S.count('D'))
if T == 2:
    if UpperSub + DownerSub < S.count('?'):
        print(abs(UpperSub + DownerSub - S.count('?')) % 2)
        exit(0)
qu = S.count('?')
print(UpperSub + DownerSub + qu)
