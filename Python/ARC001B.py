A, B = map(int, input().split())

checkers = [1, -1, 5, -5, 10, -10]

turn = 0
while A != B:
    distance = [abs(B - (A + dos)) for dos in checkers]
    i = distance.index(min(distance))
    A += checkers[i]
    turn += 1
print(turn)
