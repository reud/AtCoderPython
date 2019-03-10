A, B = map(int, input().split())
binaryA = bin(A)[2::]
binaryB = bin(B)[2::]
numAlis = [0 for _ in range(len(binaryA))]
numBlis = [0 for _ in range(len(binaryB))]

keta = 1
print(range(len(binaryA)))
for key in reversed(range(len(binaryA))):
    if binaryA[key] == '0':
        if keta == 1:
            numAlis[key] = 1
        else:
            numAlis[key] = numAlis[key+1]
    if binaryA[key] == '1':
        if keta == 1:
            numAlis[key] = 2
        else:
            numAlis[key] = numAlis[key+1]+keta
    keta*=2


keta = 1
for key in reversed(range(len(binaryB))):
    if binaryB[key] == '0':
        if keta == 1:
            numBlis[key] = 1
        else:
            numBlis[key] = numBlis[key+1]
    if binaryB[key] == '1':
        if keta == 1:
            numBlis[key] = 2
        else:
            numBlis[key] = numBlis[key+1]+keta
    keta*=2

ans=0
print(numAlis)
print(numBlis)
while len(numAlis)!=len(numBlis):
    states=numBlis.pop(0)
    if states>2**(len(numAlis)):
        states-=2**(len(numAlis))
        if states%2==1:
            ans+=2**(len(numAlis))
print(numAlis)
print(numBlis)
for scope in range(len(numAlis)):
    walk=numAlis[scope]-1
    isplus=False
    while walk!=numBlis[scope]:
        print('target: {}'.format(numBlis[scope]))
        walk+=1
        if walk==(2**(len(numAlis)-scope))+1:
            print('walk is {} scope {} so turned'.format(walk,scope))
            walk=0
        elif walk-(2**(len(numAlis)-scope-1))>0:
            print('walk is {} scope {} so add'.format(walk,scope))
            isplus= not isplus

    if isplus:
        ans+=2**(len(numAlis)-scope-1)
        print(2**(len(numAlis)-scope-1))


print(ans)