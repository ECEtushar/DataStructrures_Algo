from Implementation import Graph

def dfsRec(adj,src,vl):
    vl[src]=True
    print(src,end=' ')
    for i in adj[src]:
        if vl[i] == False:
            dfsRec(adj,i,vl)

def DFS(adj,src):
    vl=[False]*len(adj)
    dfsRec(adj,src,vl)
g=Graph(4)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(3,2)


DFS(g.graph,1)
