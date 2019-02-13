alphabets = [i for i in range(ord('a'), ord('z') + 1)]
lists = [ord(i) for i in input()]
lists=list(set(lists))
lists.sort()
for i in range(len(alphabets)):
    if i+1>=len(lists) and i!=25:
        if alphabets[i] == lists[i]:
            print(chr(alphabets[i+1]))
            exit(0)
    if alphabets[i]!=lists[i]:
        print(chr(alphabets[i]))
        exit(0)


print('None')
