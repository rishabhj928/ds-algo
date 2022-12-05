
# Given a Directed Acyclic Graph (DAG), print linear ordering of vertices such that for every
# directed edge u->v, vertex u comes before v in the ordering
# Time O(V), Space O(V+E) 

from collections import defaultdict
class Graph:
    def __init__(self, vertices: int):
        self.vertices = vertices
        self.graph = defaultdict(list)
    
    def addEdge(self, x: int, y: int) -> None:
        self.graph[x].append(y)
    
    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.topologicalSortUtil(i, visited, stack)
        stack.append(v)

    def topologicalSort(self):
        visited = [False]*self.vertices
        stack = []
        for i in range(self.vertices):
            if not visited[i]:
                self.topologicalSortUtil(i, visited, stack)
        print(stack[::-1])

g = Graph(7)
g.addEdge(7, 6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
g.topologicalSort()
