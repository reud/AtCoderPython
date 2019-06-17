N=int(input())
goods=[]
for i in range(N):
    goods.append(int(input()))
expensive=max(goods)
sum=expensive/2
goods.remove(max(goods))
for i in range(N-1):
    sum+=goods[i]
print(int(sum))