N=int(input())
cards=list(map(int,input().split()))
cards.sort(reverse=True)

Alice_score=0
Bob_score=0

isAliceTurn=True
for i in range(N):
    if(isAliceTurn):
        Alice_score+=cards.pop(0)
    else:
        Bob_score+=cards.pop(0)
    isAliceTurn = not isAliceTurn

print(Alice_score-Bob_score)