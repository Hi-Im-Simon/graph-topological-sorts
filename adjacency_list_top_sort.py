from collections import defaultdict

class Graph:

    def __init__(self,n):
        self.graph = defaultdict(list)
        self.n = n

    def edge(self,v,u):
        self.graph[v].append(u)

    def topSortDFS2(self, v, checked, checkedstack):
        checked[v] = 1
        for nb in self.graph[v]:
            if checked[nb] == 0:
                self.topSortDFS2(nb, checked, checkedstack)

        checkedstack.append(v)


    def topSortDFS(self):

        checked = [0] * (self.n + 1)
        checkedstack = []

        for vert in range(1,self.n + 1):
            if checked[vert] == 0:
                self.topSortDFS2(vert,checked,checkedstack)

        return checkedstack[::-1]
