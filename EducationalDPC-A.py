from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
import numpy as np
node_num = int(input())
nodes=input().split()




route_list=np.zeros((node_num,node_num))


mi_count=0
for i in range(node_num-1):
    if i+2<node_num:
        route_list[i][i+1]=abs(int(nodes[i+1])-int(nodes[i])) if abs(int(nodes[i+1])-int(nodes[i])) != 0 else 0.0000001
        route_list[i][i+2]=abs(int(nodes[i+2])-int(nodes[i])) if abs(int(nodes[i+2])-int(nodes[i])) != 0 else 0.0000001
    else:
        route_list[i][i+1]=abs(int(nodes[i+1])-int(nodes[i])) if abs(int(nodes[i+1])-int(nodes[i])) != 0 else 0.0000001


route_list = csr_matrix(route_list)
#print(route_list)
dist_matrix= dijkstra(csgraph=route_list, directed=False, indices=0, return_predecessors=False)

dis=dist_matrix[-1]

print(int(dis))