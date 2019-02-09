L=int(input())
lists=[]
for i in range(L):
    s=int(input())
    lists.append(s%2+1 if s!=0 else 0)

print(lists)