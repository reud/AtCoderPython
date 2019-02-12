a, b = input().split()
num = int(a + b)
answers = []
key = 1
while True:
    answers.append(key * key)
    key += 1
    if key == 5999:
        break

print('Yes' if num in answers else 'No')
