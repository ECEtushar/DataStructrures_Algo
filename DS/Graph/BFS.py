from Implementation import Graph

def BFS(adList,src):
    
    if len(adList)==0:
        return None
    from collections import deque
    vertex=[False]*len(adList)
    q=deque()
    q.append(src)
    vertex[src]=True
    while len(q)!=0:
        v=q.popleft()
        print(v,end=' ')
        for i in adList[v]:
            if vertex[i]==False:
                q.append(i)
                vertex[i]=True
    




g=Graph(5)
g.addEdge(0,4)
g.addEdge(4,1)
g.addEdge(4,3)
g.addEdge(1,2)
g.addEdge(2,3)

#g.showGraph()

#BFS(g.graph,4)