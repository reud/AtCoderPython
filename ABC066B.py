S = input()
S = '.'.join([S[i] for i in range(len(S) - 2)]).replace('.', '')
while True:
    former = '.'.join([S[i] for i in range(int(len(S) / 2))]).replace('.', '')
    latter = '.'.join([S[i] for i in range(int(len(S) / 2), len(S))]).replace('.', '')
    if former ==latter:
        print(len(former)*2)
        exit(0)
    else:
        S = '.'.join([S[i] for i in range(len(S) - 2)]).replace('.', '')

