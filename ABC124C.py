def count(li, first):
    if first == '0':
        isZero = True
    else:
        isZero = False
    counter = 0
    for i in li[1:]:
        if i == '0' and isZero:
            counter += 1
            isZero = False
        elif i == '1' and (not isZero):
            counter += 1
            isZero = True
        else:
            isZero = not isZero
    return counter


S = input()

print(min([count(list(S), S[0]), count(list(S)[::-1], list(S)[::-1][0])]))
