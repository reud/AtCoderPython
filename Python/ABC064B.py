N = int(input())
A = [int(a) for a in input().split()]
A = list(set(A))
A.sort()
print(max(A)-min(A))
