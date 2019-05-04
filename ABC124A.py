li = [int(a) for a in input().split()]
print(max(li) + max(li) - 1) if li[0]!=li[1] else print(max(li)*2)
