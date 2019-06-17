import math
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

mli = [A % 10 if A % 10 != 0 else 999, B % 10 if B % 10 != 0 else 999, C % 10 if C % 10 != 0 else 999,
      D % 10 if D % 10 != 0 else 999, E % 10 if E % 10 != 0 else 999]

last=mli.index(min(mli))

li=[A,B,C,D,E]

for i in range(len(li)):
      if last==i:
            pass
      else:
            li[i]=math.ceil(float(li[i]/10))*10
print(sum(li))


