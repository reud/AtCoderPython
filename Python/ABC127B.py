r,D,twokx = map(int,input().split())
x=twokx

for _ in range(10):
    val = r * x - D
    print(val)
    x=val