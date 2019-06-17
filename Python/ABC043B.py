s=input()

while s.replace('0B','').replace('1B','') != s:
    s=s.replace('0B', '').replace('1B', '')
print(s.replace('B',''))