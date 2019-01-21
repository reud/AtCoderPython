
N,K=map(int,input().split())

def get_duplicate_list(seq,index):
    seen = []
    return [x[index] for x in seq if not seen.append(x[index]) and seen.count(x[index]) == 2]

t=[0 for _ in range(N)]
d=[0 for _ in range(N)]
key=[i for i in range(N)]
sushi=[]
for i in range(N):
    t[i],d[i]=map(int,input().split())
    sushi.append([t[i],d[i]])

sorted_sushi=sorted(sushi,key= lambda x:x[1])
#print(sorted_sushi)
taberu=[]
for i in range(K):
    taberu.append(sorted_sushi.pop())

sorted_taberu = sorted ( taberu, key=lambda x: -x[ 1 ] )
maxscore=0
for i in range(N):
    # 重複要素をだす
    if len(set([x[0] for x in sorted_taberu])) ** 2 + sum ( [x[1] for x in sorted_taberu]) >maxscore:
        maxscore=len(set([x[0] for x in sorted_taberu])) ** 2 + sum ( [x[1] for x in sorted_taberu])
    sorted_sushi = sorted ( sorted_sushi, key=lambda x: x[ 1 ] )
    sorted_taberu = sorted ( sorted_taberu, key=lambda x: -x[ 1 ],reverse=True )
    dp=get_duplicate_list(sorted_taberu,0)
    '''
    print('pop taberu \n')
    print('sushi')
    print(sorted_sushi)
    print('taberu')
    print(sorted_taberu)
    print('\n\n')
    '''
    if not dp:
        if len ( set ( [ x[ 0 ] for x in sorted_taberu ] ) ) ** 2 + sum (
                [ x[ 1 ] for x in sorted_taberu ] ) > maxscore:
            maxscore = len ( set ( [ x[ 0 ] for x in sorted_taberu ] ) ) ** 2 + sum (
                [ x[ 1 ] for x in sorted_taberu ] )
        continue
    else:
        sb=False
        for i in range(len(sorted_taberu)):
            for s in dp:
                if sorted_taberu[i][0]==s:
                    sorted_sushi.append(sorted_taberu.pop(i))
                    sb=True
                    break
            if sb:
                break
    sorted_sushi = sorted ( sorted_sushi, key=lambda x: x[ 1 ] )
    sb=False
    '''
    print('push taberu \n')
    print('sushi')
    print(sorted_sushi)
    print('taberu')
    print(sorted_taberu)
    print('\n\n')
    '''
    for i in range(len(sorted_sushi)):
        setted_sushi=set([x[0] for x in sorted_sushi])
        setted_taberu=set([x[0] for x in sorted_taberu])

        seki=setted_sushi & setted_taberu

        if not seki:
            sorted_taberu.append(sorted_sushi.pop())
            if len ( set ( [ x[ 0 ] for x in sorted_taberu ] ) ) ** 2 + sum (
                    [ x[ 1 ] for x in sorted_taberu ] ) > maxscore:
                maxscore = len ( set ( [ x[ 0 ] for x in sorted_taberu ] ) ) ** 2 + sum (
                    [ x[ 1 ] for x in sorted_taberu ] )
                sb=True
                break

        for i in range(len(sorted_sushi)):
            for s in list(seki):
                if sorted_sushi[i][0]!=seki:
                    sb=True
                    sorted_taberu.append ( sorted_sushi.pop (i ) )
                    break
            if sb:
                break
        if sb:
            break




print (maxscore)
exit ( 0 )




