N,A,B=map(int,input().split())
print('{0} {1}'.format(min(A,B),0 if (A+B)-N<0 else (A+B)-N))