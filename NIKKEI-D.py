class Node(object):
    def __init__(self,point):
        self.point=point
        self.child=[]
        self.parent=[]
    def addpar(self,parent):
        self.parent.append(parent)
    def addchi( self,child ):
        self.child.append(child)
    def bigdaddy( self ):
        return True if len(self.parent)>1 else False

    def __str__(self):
        return 'node:{0} parents:{1} childs{2} '.format(self.point,self.parent,self.child)

N,M=map(int,input().split())
nodes=[Node(i) for i in range(1,N+1)]

keys=[]
for i in range(N-1+M):
    a,b=map(int,input().split())
    nodes[a-1].addchi(b)
    nodes[b-1].addpar(a)
    if nodes[b-1].bigdaddy():
        if b-1 not in keys:
            keys.append(b-1)


def solve(key,nodes,root,sticks=-1,dist=0,start=False):
    #print(nodes[key])
    if key+1 ==root :
        #print('fin')
        return dist
    elif len(nodes[key].parent)==1:
        return solve(nodes[key].parent[0]-1,nodes,root,-1,dist+1)
    else:
        if start:
            #print('sticks {} nextpoint {} parent{}'.format(sticks,nodes[sticks-1].point,nodes[sticks-1].parent))
            if not nodes[sticks-1].parent:
                return 0
            return solve(nodes[sticks-1].parent[0]-1,nodes,root,-1,dist+1)
        else:
            #print('cant')
            #print(nodes[key])
            return -1

def getroot(nodes,key=1):
    if nodes[key].parent:
        return getroot(nodes,nodes[key].parent[0]-1)
    else:
        return key+1



rootkey=getroot(nodes)

#print('\n\n')
#print('rootkey{}'.format(rootkey))
while keys:
    key=keys.pop()
    #print('kaburi')
    #print(nodes[key])
    maxi=-1
    maxd=-1
    for i in nodes[key].parent:
        #print('i:{}'.format(i))
        ace=solve(key,nodes,rootkey,i,0,True)
        #print('distance {}'.format(ace))
        if maxd<ace:
            maxd=ace
            maxi=i
    nodes[ key ].parent=[maxi]


for i in range(N):
    print(nodes[i].parent[0] if nodes[i].parent else 0)