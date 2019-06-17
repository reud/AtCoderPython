N=int(input())
S=input()
score=1
mozis='abcdefghijklmnopqrstuvwxyz'
for i in mozis:
    point=S.count(i)+1
    score*=point

print((score-1)%(10**9+7))