S=input()

dusted=False
cont=False
line='keyence'
find=S.find('keyence')
rfind=S.rfind('keyence')
print('find {} rfind {}'.format(find,rfind))
if  find == 0 or rfind==len(S)-7:
    print('YES')
    exit(0)
elif find != -1:
    print('NO')
    exit(0)

fs=True
line=''
for i in S:
    print('{} and ds:{} cont:{} line:{}'.format(i,dusted,cont,line))
    if i!='k' and i!='y' and i!='e' and i!='n' and i!='c':
        if dusted:
            if cont:
                pass
            else:
                print('NO')
                exit(0)
        else:
            dusted=True
            cont=True
    else:
        if line=='':
            if i!='k':
                if dusted:
                    if cont:
                        pass
                    else:
                        print ( 'NO' )
                        exit ( 0 )
                else:
                    dusted = True
            else:
                line+='k'
                cont=False
        elif line=='k':
            if i!='e':
                if dusted:
                    if cont:
                        pass
                    else:
                        print ( 'NO' )
                        exit ( 0 )
                else:
                    dusted = True
            else:
                line+='e'
                cont=False
        elif line=='ke':
            if i!='y':
                if dusted:
                    if cont:
                        pass
                    else:
                        print ( 'NO' )
                        exit ( 0 )
                else:
                    dusted = True
            else:
                line+='y'
                cont=False
        elif line=='key':
            if i!='e':
                if dusted:
                    if cont:
                        pass
                    else:
                        print ( 'NO' )
                        exit ( 0 )
                else:
                    dusted = True
            else:
                line+='e'
                cont=False
        elif line=='keye':
            if i!='n':
                if dusted:
                    if cont:
                        pass
                    else:
                        print ( 'NO' )
                        exit ( 0 )
                else:
                    dusted = True
            else:
                line+='n'
                cont=False
        elif line=='keyen':
            if i!='c':
                if dusted:
                    if cont:
                        pass
                    else:
                        print ( 'NO' )
                        exit ( 0 )
                else:
                    dusted = True
            else:
                line+='c'
                cont=False
        elif line=='keyenc':
            if i!='e':
                if dusted:
                    if cont:
                        pass
                    else:
                        print ( 'NO' )
                        exit ( 0 )
                else:
                    dusted = True
            else:
                line+='e'
                cont=False
        elif line=='keyence':
            if dusted:
                if cont:
                    pass
                else:
                    print ( 'NO' )
                    exit ( 0 )
            else:
                dusted = True
    if dusted:
        if fs:
            fs=False
            cont=True

print('YES' if line=='keyence' else 'NO')