class Graph:
    def __init__(self,vertices):
        self.graph=[[] for i in range(vertices)]


    def showGraph(self):
        for i in range(len(self.graph)):
            print(f'{i}:{self.graph[i]}')

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
if __name__=='__main__':
    gp=Graph(4)
    gp.addEdge(0,1)
    gp.addEdge(0,2)
    gp.addEdge(1,2)
    gp.addEdge(2,3)
    gp.showGraph()
    