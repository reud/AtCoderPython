S = input ( )

dusted = False
cont = False
line = 'keyence'
find = S.find ( 'keyence' )
rfind = S.rfind ( 'keyence' )
#print ( 'find {} rfind {}'.format ( find, rfind ) )
if find == 0 or rfind == len ( S ) - 7:
    print ( 'YES' )
    exit ( 0 )
elif find != -1:
    print ( 'NO' )
    exit ( 0 )

fs = True
line = ''
keyence = [ c for c in "keyence" ]
a_err=False
b_err=False
keyence2='keyence'
count=0
for i in range(len ( S )):

    #print ( keyence )
    #print ( 'i {} ri {}'.format ( S[i], S[len(S)-1-i] ) )
    try:
        if not  b_err:
            #print ( 'key2 {} S {}'.format ( keyence2[ 6 - i ], S[ len ( S ) - 1 - i ] ) )

            if keyence2[ 6 - i ] != S[ len ( S ) - 1 - i ]:
                b_err=True
            if not b_err:
                keyence.remove ( S[len(S)-1-i] )

            count+=1

    except ValueError:
        b_err=True

    if not keyence:
        print ( 'YES' )
        exit ( 0 )
    try:
        if not a_err:
            if keyence2[ i ] != S[ i]:
                a_err=True
            if not a_err:
                keyence.remove ( S[i] )
    except ValueError:
        a_err=True

    if a_err and b_err:
        print('NO')
        exit(0)

    if not keyence:
        print ( 'YES' )
        exit ( 0 )

