import sys
cap=int(input())
word_list=[str(input()) for i in range(cap)]

#check Duplication
li_uniq = list(set(word_list))
if( not len(li_uniq)==len(word_list) ):
    print ('No')
    sys.exit()
lastc=word_list[0][0:1]
for string in word_list:
    if(not string[0:1]==lastc):
        print('No')
        sys.exit()
    lastc = string[-1:]
print('Yes')
