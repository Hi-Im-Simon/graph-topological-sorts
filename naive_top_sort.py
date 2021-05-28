from collections import defaultdict


class Graph:

    def __init__(self,n):
        self.graph = defaultdict(list)
        self.n = n

    def edge(self,v,u):
        self.graph[v].append(u)

    def topSort(self):

        inDeg =[0] * (self.n+1)

        for i in self.graph:
            for j in self.graph[i]:
                inDeg[j] += 1

        queue = list()
        for i in range(1,self.n+1):
            if inDeg[i] == 0:
                queue.append(i)

        topsort = list()

        for vert in queue:
            topsort.append(vert)
            for nb in self.graph[vert]:
                inDeg[nb] -= 1
                if inDeg[nb] == 0:
                    queue.append(nb)
        return topsort
