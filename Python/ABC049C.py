line=input()
if not line:
    print('YES')
    exit(0)
while(line):
    if(line[:11]=='dreameraser'):
        line=line.replace('dream','',1)
    elif (line[:10] == 'dreamerase'):
        line = line.replace('dream', '', 1)
    elif(line[:7]=='dreamer'):
        line=line.replace('dreamer','',1)
    elif(line[:6]=='eraser'):
        line=line.replace('eraser','',1)
    elif(line[:5]=='dream'):
        line=line.replace('dream','',1)
    elif(line[:5]=='erase'):
        line=line.replace('erase','',1)
    else:
        if(line):
            print('NO')
            exit(0)


print('YES')
exit(0)