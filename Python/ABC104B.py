S=input()

start_S_flag=False
like_Center_C_flag=False
if S[0]!='A':
    print('WA')
    exit(0)

kaburi=False
for i in range(len(S)):
    #print(i)
    if S[i].isupper() and i>0:
        if S[i]=='C' and i>=2 and i<=(len(S)-2) and not kaburi:
            kaburi=True
            like_Center_C_flag=True
        else:
            print ( 'WA' )
            exit ( 0 )
if kaburi:
    print ( 'AC' )
else:
    print('WA')