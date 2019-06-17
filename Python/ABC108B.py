x1, y1, x2, y2 = map(int, input().split())


def addrad(a, b):
    return -b, a


# B 0 base and get C with addrad*3

x = x1 - x2
y = y1 - y2
x, y = addrad(x, y)
x, y = addrad(x, y)
x, y = addrad(x, y)
x += x2
y += y2
cx = x
cy = y

# A 0 base and get D with addrad*1
x = x2 - x1
y = y2 - y1
x, y = addrad(x, y)
x += x1
y += y1
dx = x
dy = y
print('{} {} {} {}'.format(cx, cy, dx, dy))