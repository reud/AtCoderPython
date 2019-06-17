W, a, b = map(int, input().split())

apos = [a, a + W]
bpos = [b, b + W]

secis_left = False if bpos[1] > apos[1] else True
if bpos[0] - apos[1] <= 0 and not secis_left:
    print(0)
    exit(0)
elif apos[0] - bpos[1] <= 0 and secis_left:
    print(0)
    exit(0)

dist = [abs(apos[0] - bpos[1]), abs(bpos[0] - apos[1])]

print(min(dist))
