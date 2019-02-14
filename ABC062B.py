H, W = map(int, input().split())
A = [[a for a in input()] for _ in range(H)]
Sharps = [ ['#' for i in range(W+2)]for _ in range(H + 2)]
for i in range(1,H+1):
    for j in range(1,W+1):
        Sharps[i][j]=A[i-1][j-1]


for i in Sharps:
    print('.'.join(i).replace('.',''))