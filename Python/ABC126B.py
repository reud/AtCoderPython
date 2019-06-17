S=input()
mae=int(S[0]+S[1])
usiro=int(S[2]+S[3])

maeMM = True if 0< mae and mae<13 else False
usiroMM =True if 0< usiro and usiro<13 else False

if maeMM and usiroMM:
    print('AMBIGUOUS')
elif maeMM:
    print('MMYY')
elif usiroMM:
    print('YYMM')
else:
    print('NA')