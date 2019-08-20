W,H,x,y=map(int,input().split())
# 全部半分になるはず
ans = (W*H)/2
if W/2 == x and H/2 == y:
    print('{} {}'.format(ans,1))
else:
    print('{} {}'.format(ans,0))
