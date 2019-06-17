print('YES' if (lambda lists=input().split(): True if lists[0][-1] == lists[1][0] and lists[1][-1] == lists[2][0] else False )() else 'NO')
