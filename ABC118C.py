import copy
N = int(input())
A = [int(i) for i in input().split()]
A=list(set(A))
A.sort()

while True:
    B=copy.deepcopy(A)
    for i in range(1, len(A)):
        A[i] = A[i] % A[0] if not A[i] % A[0] ==0 else A[i]

    if B==A or len(A)==1:
        print(min(A))
        exit(0)
    A = list(set(A))
    A.sort()
