# ABC062C - Chocolate Bar

H, W = map(int, input().split())

Ans = 99999999999999999
# Three Division Pattern
TDPAns = min((1 if H % 3 != 0 else 0) * W, (1 if W % 3 != 0 else 0) * H)

OTDPAns = Ans
TODPAns = Ans

# One Two Division Pattern
for x in range(1, W + 1):
    width = W - x
    row_mass = x * H
    sub = Ans
    if H % 2 == 0:
        y = H // 2
        sub = max(row_mass, (width * y)) - min(row_mass, (width * y))
    else:
        y1 = (H // 2) + 1
        y2 = (H // 2)
        sub = max(row_mass, (width * y1), (width * y2)) - min(row_mass, (width * y1), (width * y2))

    OTDPAns = min(OTDPAns, sub)

# Two One Division Pattern
for y in range(1, H + 1):
    height = H - y
    line_mass = height * W
    sub = Ans
    if W % 2 == 0:
        x = W // 2
        sub = max(line_mass, x * y) - min(line_mass, x * y)
    else:
        x1 = (W // 2) + 1
        x2 = (W // 2)
        sub = max(line_mass, x1 * y, x2 * y) - min(line_mass, x1 * y, x2 * y)
    TODPAns = min(TODPAns, sub)

# print(f'{TDPAns}, {OTDPAns}, {TODPAns}')
print(min(TDPAns, OTDPAns, TODPAns))
