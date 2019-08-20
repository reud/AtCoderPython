import math
N,K=map(int,input().split())
RED=N-K
results=[]

results.append(0)
for i in range(1,K+1):
    leng = N-K+i
    Lonely_Blue = i-1
    if i==K:
        Lonely_Blue+=1
        results.append(
            int(math.factorial(leng) / (math.factorial(Lonely_Blue) * math.factorial(RED))) - (sum(results)))
    if i!=1:
        gainer = int(math.factorial(leng-1)/(math.factorial(RED)*math.factorial(Lonely_Blue-1)))*2
        results.append(int(math.factorial(leng)/(math.factorial(Lonely_Blue)*math.factorial(RED)))-gainer)
    else:
        results.append(int(math.factorial(leng) / (math.factorial(Lonely_Blue) * math.factorial(RED))))

for r in range(1,len(results)-1):
    print(results[r]%(10**9+7))
