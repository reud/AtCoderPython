N=int(input())
Ryuka=[]
for i in range(87):
    if i==0:
        Ryuka.append(2)
    elif i==1:
        Ryuka.append(1)
    else:
        Ryuka.append(Ryuka[i-1]+Ryuka[i-2])

print(Ryuka[N])