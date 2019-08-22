N = int(input())
connections = [ [] for _ in range(N + 1)]
for i in range(2, N + 1):
    c = int(input())
    connections[c].append(i)
    connections[i].append(c)

salarys = [0] * (N + 1)



for i in reversed(range(1, N + 1)):
    bukas = []
    bukas_salary = []
    for ci in range(len(connections[i])):
        if connections[i][ci] > i:
            bukas.append(connections[i][ci])
            bukas_salary.append(salarys[connections[i][ci]])
    # print(f'社員{i}のconnection{connections[i]}')
    if not bukas:
        salarys[i] = 1
    else:
        salarys[i] = max(bukas_salary)+min(bukas_salary)+1


print(salarys[1])
