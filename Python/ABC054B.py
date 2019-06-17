N, M = map(int, input().split())
A = [[ch for ch in input()] for _ in range(N)]
B = [[ch for ch in input()] for _ in range(M)]
for ai in range(len(A)-len(B)+1):
    for aj in range(len(A)-len(B)+1):
        trimmed=[]
        for i_trimmer in range(ai,ai+len(B)):
            line=[]
            for j_trimmer in range(aj,aj+len(B)):
                line.append(A[i_trimmer][j_trimmer])
            trimmed.append(line)
        if trimmed==B:
            print('Yes')
            exit(0)

print('No')
