X=int(input())
anss=[]
for i in range(1000):
    anss.append(i**4)


for i in range(len(anss)):
    if X==anss[i]:
        print(i)
        exit(0)