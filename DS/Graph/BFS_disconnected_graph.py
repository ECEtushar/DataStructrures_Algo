'''
This is the implementation of BFS if a source of graph is not given and graph may be disconnecetd
'''
from Implementation import Graph

def BFS(adj,src,visited):
    from collections import deque
    q=deque()
    q.append(src)
    visited[src]=True
    while q:
        curr=q.popleft()
        print(curr,end=' ')
        for i in adj[curr]:
            if visited[i] is False:
                q.append(i)
                visited[i]=True


def BFS_D(adj):
    VL=[False]*len(adj)
    for i in range(len(adj)):
        if VL[i] is False:
            BFS(adj,i,VL)

g=Graph(5)
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(0,2)
g.addEdge(3,4)
g.showGraph()
print('\n')
print('BFS Traversal:',end=' ')
BFS_D(g.graph)