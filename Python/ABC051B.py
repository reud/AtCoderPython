K, S = map(int, input().split())
count = 0
for x in range(K+1):
    for y in range(K+1):
        z = S - x - y
        if x + y + z == S and 0 <= z <= K:
            #print('{} {} {}'.format(x,y,z))
            count += 1

print(count)
