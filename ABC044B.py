w=[i for i in input()]
print('Yes' if all([True if w.count(ch)%2==0 else False for ch in 'abcdefghijklmnopqrstuvwxyz']) else 'No')