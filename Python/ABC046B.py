N, K = map(int, input().split())

if N==1:
    print(K)
    exit(0)
else:
    print(K*((K-1)**(N-1)))