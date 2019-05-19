import copy
import sys

sys.setrecursionlimit(10000000)
N=int(input())
data=[[int(i) for i in input().split()] for _ in range(N-1)]
state = [-1 for _ in range(N+1)]
def search(depth,copyed_state):
    if depth==len(data):
        # print('end')
        return copyed_state
    kl = data[depth]
    anss=[]
    # print('depth:{} state:{}'.format(depth,copyed_state))
    if kl[2]%2 ==0:
        if copyed_state[kl[0]]==-1 and copyed_state[kl[1]]==-1:
            new_lizeros = copy.copy(copyed_state)
            new_lizeros[kl[0]] = 0
            new_lizeros[kl[1]] = 0
            anss.append(search(depth+1,new_lizeros))
            new_liones = copy.copy(copyed_state)
            new_liones[kl[0]] = 1
            new_liones[kl[1]] = 1
            anss.append(search(depth+1,new_liones))
        elif copyed_state[kl[0]]==0 and copyed_state[kl[1]]==-1:
            one_lizeros = copy.copy(copyed_state)
            one_lizeros[kl[1]] = 0
            anss.append(search(depth+1,one_lizeros))
        elif copyed_state[kl[0]]==1 and copyed_state[kl[1]]==-1:
            one_lizeros = copy.copy(copyed_state)
            one_lizeros[kl[1]] = 1
            anss.append(search(depth+1,one_lizeros))
        elif copyed_state[kl[0]]==-1 and copyed_state[kl[1]]==0:
            one_lizeros = copy.copy(copyed_state)
            one_lizeros[kl[0]] = 0
            anss.append(search(depth+1,one_lizeros))
        elif copyed_state[kl[0]]==-1 and copyed_state[kl[1]]==1:
            one_lizeros = copy.copy(copyed_state)
            one_lizeros[kl[0]] = 1
            anss.append(search(depth+1,one_lizeros))
    for i in anss:
        if len(i)!=0:
            return i
    if copyed_state[kl[0]] == -1 and copyed_state[kl[1]] == -1:
        new_lizeros2 = copy.copy(copyed_state)
        new_lizeros2[kl[0]] = 0
        new_lizeros2[kl[1]] = 1
        anss.append(search(depth + 1, new_lizeros2))
        new_liones2 = copy.copy(copyed_state)
        new_liones2[kl[0]] = 1
        new_liones2[kl[1]] = 0
        anss.append(search(depth + 1, new_liones2))
    elif copyed_state[kl[0]] == 0 and copyed_state[kl[1]] == -1:
        one_lizeros2 = copy.copy(copyed_state)
        one_lizeros2[kl[1]] = 1
        anss.append(search(depth + 1, one_lizeros2))
    elif copyed_state[kl[0]] == 1 and copyed_state[kl[1]] == -1:
        one_lizeros2 = copy.copy(copyed_state)
        one_lizeros2[kl[1]] = 0
        anss.append(search(depth + 1, one_lizeros2))
    elif copyed_state[kl[0]] == -1 and copyed_state[kl[1]] == 0:
        one_lizeros2 = copy.copy(copyed_state)
        one_lizeros2[kl[0]] = 1
        anss.append(search(depth + 1, one_lizeros2))
    elif copyed_state[kl[0]] == -1 and copyed_state[kl[1]] == 1:
        one_lizeros2 = copy.copy(copyed_state)
        one_lizeros2[kl[0]] = 0
        anss.append(search(depth + 1, one_lizeros2))
    else: # dottimo haittetara
        sktyu = copy.copy(copyed_state)
        anss.append(search(depth + 1, sktyu))

    for i in anss:
        if len(i)!=0:
            return i
ans=search(0,state)
for i in range(1,N+1):
    print(ans[i])
