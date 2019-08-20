N=int(input())
tasks=[]
for _ in range(N):
    A,B=map(int,input().split())
    tasks.append((A,B))
tasks.sort(key=lambda x:x[1])

time=0
for task in tasks:
    time+=task[0]
    if task[1]-time>=0:
        pass
    else:
        print('No')
        exit(0)
print('Yes')
