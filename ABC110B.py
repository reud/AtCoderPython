N,M,X,Y=map(int,input().split())
x_box=input().split()
y_box=input().split()

for a in range(len(x_box)):
    x_box[a]=int(x_box[a])
for a in range(len(y_box)):
    y_box[a]=int(y_box[a])

for i in range(X+1,Y+1):
    if max(x_box)< i <=min(y_box):
        print('No War')
        exit()
print('War')