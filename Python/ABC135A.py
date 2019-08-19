A,B=map(int,input().split())
print(max(A,B)-int((max(A,B)-min(A,B))/2) if int((max(A,B)-min(A,B))/2) == (max(A,B)-min(A,B))/2 else 'IMPOSSIBLE'
)