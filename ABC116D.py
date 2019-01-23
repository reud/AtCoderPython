import  collections
class Sushi(object):
    def __init__(self,lines):
        neta,oishisa=map(int,lines.split())
        self.neta=neta
        self.oishisa=oishisa
    def __str__(self):
        return "寿司:{0} 美味しさ:{1}".format(self.neta,self.oishisa)

def score_out(eat_list):
    score=0
    items=list(collections.Counter([i.neta for i in eat_list]).items())
    score+=len(items)**2
    basic_points=[i.oishisa for i in eat_list]
    score+=sum(basic_points)

    return score

N,K=map(int,input().split())

sushi_list=[Sushi(input()) for _ in range(N)]

sushi_list=sorted(sushi_list,key= lambda  x:x.oishisa)

eat_list=[]

neta_max=len(list(collections.Counter([i.neta for i in sushi_list]).items()))


for i in range(K):
    eat_list.append(sushi_list.pop())
    print(eat_list[i])

eat_items=list(collections.Counter([i.neta for i in eat_list]).items())

if len(eat_items)==K:
    print(score_out(eat_list))
    exit(0)

low_band_types=len(eat_items)

maxscore=score_out(eat_list)
for i in range(N):
    # 寿司が全て独立しているか判断する。
    # 独立してたら終了させる。
    # 寿司屋のネタの最大種類==選択したネタが最大種類でも終了
    eat_list=sorted(eat_list,key=lambda x:x.oishisa)
    print ( '現在の寿司' )
    for i in eat_list:
        print(i)
    print('\n')

    if len(list(collections.Counter([i.neta for i in eat_list]).items()))==K and maxscore<=score_out(eat_list):
        print(score_out(eat_list))
        exit(0)
    elif len(list(collections.Counter([i.neta for i in eat_list]).items()))==neta_max and maxscore<=score_out(eat_list):
        print(score_out(eat_list))
        exit(0)

    eat_items = list ( collections.Counter ( [ i.neta for i in eat_list ] ).items ( ) )
    neta_kaburi_list=[i[0] for i in eat_items if i[1]>1]
    print(neta_kaburi_list)
    min_oishisa=-1
    kick_avails=[]
    for kaburi_neta in neta_kaburi_list:
        kick_avails+=[i for i in eat_list if i.neta==kaburi_neta]
    kick_avails=sorted(kick_avails,key=lambda x:x.oishisa)
    if not kick_avails:
        print(maxscore)
        exit(0)
    kick=kick_avails.pop()
    eat_list.remove(kick)
    sushi_list=sorted(sushi_list,key= lambda x:x.oishisa)
    ef=True
    neta_list = [ i[ 0 ] for i in eat_items ]

    if not sushi_list:
        print(maxscore)
        exit(0)


    while ef:
        eat_list = sorted ( eat_list, key=lambda x: x.oishisa,reverse=True)
        sushi=sushi_list.pop()
        print('poped sushi is ')
        print(sushi)
        if sushi.neta in neta_list:
            pass
        else:

            eat_list.append(sushi)
            ef=False

    if score_out(eat_list)>maxscore:
        maxscore=score_out(eat_list)

print(maxscore)



