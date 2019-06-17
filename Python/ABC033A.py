N = input()
key = N[0]
for i in N:
    if key != i:
        print('DIFFERENT')
        exit(0)
print('SAME')
