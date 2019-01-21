N=int(input())
h=input().split()
h.append(-1)
index=0
count=0
all_zeros=True
for i in h:
    if i!='0':
        all_zeros=False
        break

if all_zeros:
    print('0')
    exit(0)

while True:
    flag=True
    while flag:
        for i in range(index,len(h)):
            h[i]=int(h[i])
            if not h[i]-1<0:
                h[i]-=1
            elif h[index]==0:
                flag=False
                if index==i:
                    pass
                else:
                    count+=1
                break
            else:
                count += 1
                break

        #print(h)
        #print(count)
        #print('\n')
    counter=True
    while counter:
        index+=1
        if not h[index]==0:
            counter=False

    if h[index]==-1:
        print(count)
        exit(0)