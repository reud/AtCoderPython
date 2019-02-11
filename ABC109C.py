import fractions
import traceback
n,x=map(int,input().split())
citys=list(map(int, input().split()))
mod_citys=citys
for i in range(len(mod_citys)):
    mod_citys[i]-=x
    if(mod_citys[i]<0):
        mod_citys[i] *= -1
if(len(mod_citys)==1):
    print(mod_citys[0])
elif(len(mod_citys)==2):
    print(fractions.gcd(mod_citys[0],mod_citys[1]))
else:
    mod_citys = sorted(mod_citys, reverse=False)
    spmin = 9999999999999
    pod = 0
    for i in range(len(mod_citys)):
        try:
            pod=fractions.gcd(mod_citys[i],mod_citys[i+1])
            if(pod<spmin):
                spmin=pod
        except:
            pass
    print(spmin)