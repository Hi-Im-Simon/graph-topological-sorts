class Graph:

    def __init__(self, vertices):
        self.v = vertices
        self.matrix = [[0 for i in range(self.v)] for j in range(self.v)]
        self.visited = [False] * self.v

    def addEdge(self, vert1, vert2):
        self.matrix[vert1][vert2] = 1

    def DFS2(self, visited, vert, sortedgraph):
        visited[vert] = True
        for i in range(self.v):
            if self.matrix[vert][i] == 1 and not visited[i]:
                self.DFS2(visited, i, sortedgraph)
        sortedgraph.append(vert)

    def DFS(self):
        sortedgraph = []
        for vert in range(len(self.visited)):
            if not self.visited[vert]:
                self.DFS2(self.visited, vert, sortedgraph)
        return sortedgraph[::-1]
                
g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
u = g.DFS()
print(u)
