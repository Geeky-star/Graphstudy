from collections import defaultdict


class Graph:

    def __init__(self, v):

        self.vertices = v
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):

        visited[v] = True
        print(v, end=" ")
        for nbr in self.graph[v]:
            if visited[nbr] == False:
                self.DFSUtil(nbr, visited)

    def DFS(self):
        visited = [False]*self.vertices

        for vertex in list(self.graph):

            if visited[vertex] == False:
                self.DFSUtil(vertex, visited)


g = Graph(7)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(4, 1)
g.addEdge(6, 4)
g.addEdge(5, 6)
g.addEdge(5, 2)
g.addEdge(6, 0)

g.DFS()
