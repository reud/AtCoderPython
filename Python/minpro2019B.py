import copy
roads = []
roads2 = []
roads_stay = []
for s in range(3):
    a = [int(i) for i in input().split()]
    roads += [a]
lines=[]
for i in roads:
    lines.append(i[0])
    lines.append(i[1])
#print(lines)
copys=copy.deepcopy(lines)
for i in range(len(lines)):
    lines=copy.deepcopy(copys)
    form=True if i%2==0 else False
    #print(lines)
    #print('form {} i={}'.format(form,i))
    if form:
        tag=lines[i+1]
        end=[lines[i],lines[i+1]]
        lines[i]=0
        lines[i+1]=0
    else:
        tag=lines[i-1]
        end=[lines[i-1],lines[i]]
        lines[i]=0
        lines[i-1]=0
    flag=True

    while sum(lines)!=0:
        #print('us')
        if tag in lines:
            index=lines.index(tag)
            form = True if index % 2==0 else False
            if form:
                tag = lines[index + 1]
                end += [lines[index + 1]]
                lines[index] = 0
                lines[index + 1] = 0
            else:
                tag = lines[index - 1]
                end += [lines[index - 1]]
                lines[index] = 0
                lines[index - 1] = 0
        else:
            break
    if len(set(end))==4 and sum(lines)==0:
        print('YES')
        exit(0)
    #print('next')

print('NO')