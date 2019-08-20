import fractions
def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)
A,B,C,D=map(int,input().split())
A=A-1
# 1<= A-1 patern
AnC=A//C
AnD=A//D
AnCandD=A//lcm(C,D)
Aans=A-(AnC+AnD-AnCandD)
# 1<= B patern
BnC=B//C
BnD=B//D
BnCandD=B//lcm(C,D)
Bans=B-(BnC+BnD-BnCandD)

print(Bans-Aans)