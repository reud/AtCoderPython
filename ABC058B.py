O=input()
E=input()
password=''
for i in range(len(E)):
    password+=O[i]
    password+=E[i]
if len(O)!=len(E):
    password+=O[-1]

print(password)