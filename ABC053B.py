s=input()


for i in range(len(s)):
    if s[i]=='A':
        formerkey=i
        break

for i in range(len(s))[::-1]:
    if s[i]=='Z':
        latterkey=i
        break



print((latterkey+1)-(formerkey+1)+1)