s=int(input())
a=[s]
tmp=s
index=1
while True:
    if tmp%2==0:
        tmp=tmp/2
        a.append(int(tmp))
        index+=1
    else:
        tmp=tmp*3+1
        a.append(int(tmp))
        index+=1

    if len(a)!=len(list(set(a))):
        print(index)
        exit(0)
