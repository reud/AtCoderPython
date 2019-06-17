N, M = map(int, input().split())
students = [[int(i) for i in input().split()] for _ in range(N)]
checkpoints = [[int(i) for i in input().split()] for _ in range(M)]

for student in students:
    dist = []
    for checkpoint in checkpoints:
        dist.append(abs(student[0] - checkpoint[0]) + abs(student[1] - checkpoint[1]))
    print(dist.index(min(dist)) + 1)
