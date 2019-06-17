N,M=map(int,input().split())
lists=[]
back=[]
for i in range(M):
    lists.append(list(map(int, input().split()))+[i])

lists.sort(key=lambda x:x[0])
lists.sort(key=lambda x:x[1])
print(lists)


bef=0
state=0
retstr=''
triple=[]
for i in lists:
    if(i[0]!=bef):
        bef=i[0]
        state=1
        triple.append([i[0],i[1],i[2],str(i[0]).rjust(6,'0')+str(state).rjust(6,'0')])
    else:
        state+=1
        triple.append([i[0],i[1],i[2],str(i[0]).rjust(6,'0')+str(state).rjust(6,'0')])
print(triple)
triple.sort(key=lambda x:x[2])
for i in triple:
    print(i[3])


