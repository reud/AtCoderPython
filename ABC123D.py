import itertools
INF=10**11
def Searching(master_list,a_key,b_key,c_key,now_count,finish_count):
    if finish_count==now_count:
        return
    print(master_list[0][a_key]+master_list[1][b_key]+master_list[2][c_key])

    if (a_key+1)<len(Ali) and (b_key+1)<len(Bli) and (c_key+1)<len(Cli):
        diffs=[master_list[0][a_key]-master_list[0][a_key+1],
               master_list[1][b_key]-master_list[1][b_key+1],
               master_list[2][c_key]-master_list[2][c_key+1]
               ]
        id = diffs.index(min(diffs))
    elif (b_key+1)<len(Bli) and (c_key+1)<len(Cli):
        diffs=[INF,
                master_list[1][b_key]-master_list[1][b_key+1],
               master_list[2][c_key]-master_list[2][c_key+1]
               ]
        id = diffs.index(min(diffs))
    elif (a_key+1)<len(Ali) and (c_key+1)<len(Cli):
        diffs=[master_list[0][a_key]-master_list[0][a_key+1],
               INF,
               master_list[2][c_key]-master_list[2][c_key+1]
               ]
        id = diffs.index(min(diffs))

    elif (a_key+1)<len(Ali) and (b_key+1)<len(Bli):
        diffs=[master_list[0][a_key]-master_list[0][a_key+1],
               master_list[1][b_key]-master_list[1][b_key+1],
               INF
               ]
        id = diffs.index(min(diffs))
    elif (c_key+1)<len(Cli):
        id=2
    elif (b_key+1)<len(Bli):
        id=1
    elif (a_key+1)<len(Ali):
        id=0
    else:
        print('err')
        exit(1)

    if id==0:
        Searching(master_list,a_key+1,b_key,c_key,now_count+1,finish_count)
    elif id==1:
        Searching(master_list,a_key,b_key+1,c_key,now_count+1,finish_count)
    elif id==2:
        Searching(master_list,a_key,b_key,c_key+1,now_count+1,finish_count)
    else:
        print('err')
        exit(1)
    return



X,Y,Z,K=map(int,input().split())
Ali=list(map(int,input().split()))
Bli=list(map(int,input().split()))
Cli=list(map(int,input().split()))
Ali.sort(reverse=True)
Bli.sort(reverse=True)
Cli.sort(reverse=True)
if X*Y*Z<=3000:
    master = itertools.product(Ali, Bli,Cli)
    li=[]
    for ind in range(len(master)):
        li.append(ind[0]+ind[1],ind[2])
    li.sort(reverse=True)
    for i in li:
        print(i)
    exit(0)


master=itertools.product(Ali,Bli)
remaster=[ i[0]+i[1] for i in master].sort(reverse=True)[:3000]
