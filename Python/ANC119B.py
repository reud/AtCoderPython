N=int(input())
kanes=[[u for u in input().split()] for _ in range(N)]

anss=0
for kane in kanes:
    if kane[1]=='BTC':
        anss+=float(kane[0])*380000
    else:
        anss+=float(kane[0])

print(anss)