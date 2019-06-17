
N=input()
l=[]
f1=False
f2=False
f3=False
n=-1
for i in N:
    #print(i)
    if n==-1 or n!=int(i):
        #print('piu')
        f1=True
        f2=False
        f3=False
        n=int(i)
    elif n==int(i) and f1 and not f2:
        #print('poi')
        f2=True
    elif n==int(i) and f2:
        print('Yes')
        exit(0)
print('No')

