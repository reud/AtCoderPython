N=int(input())
lists=[list(map(int,input().split())) for i in range(N)]

for i in range(N):
    #print('{} {} {}'.format(lists[i][0],lists[i][1],lists[i][2]))
    substruct=lists[i][0]-(abs(lists[i][1])+abs(lists[i][2]))
    if((substruct>0 and substruct%2==0) or substruct==0):
        if(i+1<N):
            lists[i+1][0]-=lists[i][0]
            lists[i+1][1]-=lists[i][1]
            lists[i+1][2]-=lists[i][2]
    else:
        print('No')
        exit(0)
print('Yes')

