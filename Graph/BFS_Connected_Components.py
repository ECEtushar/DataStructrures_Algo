from Implementation import Graph

def BFS_D(adj,src,vis):
    from collections import deque
    q=deque()
    q.append(src)
    vis[src]=True
    while q:
        v=q.popleft()
        for i in adj[v]:
            if vis[i] is False:
                q.append(i)
                vis[i]=True

def Comp(adj):
    v=[False]*len(adj)
    res=0
    for i in range(len(adj)):
        if v[i] is False:
            BFS_D(adj,i,v)
            res+=1
    return res

g=Graph(8)
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(0,2)
g.addEdge(3,4)
g.addEdge(4,5)
g.addEdge(5,6)
g.addEdge(6,7)

print(Comp(g.graph))