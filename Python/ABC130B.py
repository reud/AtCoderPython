N,X=map(int,input().split())
ps = [int(i) for i in input().split()]
resum=0
count=1
for i in ps:
    resum += i
    if resum>X:
        break
    count+=1
print(count)
exit(0)