A=int(input())
B=int(input())
C=int(input())
X=int(input())
count=0
for big in range(0,A+1):
    for middle in range(0,B+1):
        for mini in range(0,C+1):
            kakaku=big*500+middle*100+mini*50
            if kakaku==X:
                count+=1
print(count)