A = [i for i in input()]
B = [i for i in input()]
C = [i for i in input()]

turn = 'a'
while True:

    if turn == 'a':
        try:
            turn = A.pop(0)
        except:
            print('A')
            exit(0)
    elif turn == 'b':
        try:
            turn = B.pop(0)
        except:
            print('B')
            exit(0)
    elif turn == 'c':
        try:
            turn = C.pop(0)
        except:
            print('C')
            exit(0)



