A, B, C, D = map(int, input().split())
Alice = {s for s in range(A, B + 1)}
Bob = {s for s in range(C, D + 1)}

print(len(Alice & Bob) - 1 if len(Alice & Bob) != 0 else 0)
