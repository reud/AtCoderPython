print('YES' if (lambda poles=input().split(): True if (int(poles[1])-input(poles[0]))==(int(poles[2])-input(poles[1])) else False)() else 'NO')