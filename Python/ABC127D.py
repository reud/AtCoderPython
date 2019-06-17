N,M=map(int,input().split())
As=[int(i) for i in input().split()]
As.sort()
BCS=[]
max_touch=0
for _ in range(M):
    BC=[int(i) for i in input().split()]
    max_touch = max(max_touch,BC[1])
    BCS.append(BC)

# Asから変更可能性がある部分だけ切り出し
last_key=0 # max_touch>=A[last_key]を最尾に満たす
while True:
    if last_key>len(As)-1:
        last_key=len(As)-1
        break
    if As[last_key]>max_touch:
        last_key-=1
        break
    else:
        last_key+=1

sliced=As[:last_key+1]
score=sum(As[last_key+1:])
# print(sliced)

BCS.sort(key=lambda x: x[1],reverse=True)

# print(BCS,': score:',score)

for bc in BCS:
    b=bc[0]
    c=bc[1]
    now_b=0
    d_break=False
    remover=[]
    # print('s')
    # print(sliced)
    for i in range(len(sliced)):
        if b==now_b:
            break
        elif sliced[i]>=c:
            # print('d')
            # print(sliced)
            # print(sliced[i])
            d_break=True
            break
        else:
            remover.append(sliced[i])
            now_b+=1
            # print('score add',c)
            score+=c

    for i in remover:
        sliced.remove(i)
    if d_break:
        break
print(sum(sliced)+score)