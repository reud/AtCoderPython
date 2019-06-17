N=int(input())
list1=[input() for i in range(N)]
list1_uniq=list(set(list1))
print(len(list1_uniq))