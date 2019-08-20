N = int(input())
ds = [int(n) for n in input().split()]
ds.sort()

left_key = ds[int(N/2-1)]
right_key = ds[int(N/2)]
print(right_key-left_key)
