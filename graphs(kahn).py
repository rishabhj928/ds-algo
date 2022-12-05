
from collections import defaultdict

class Graph:
    def __init__(self, v: int) -> None:
        self.graph = defaultdict(list)
        self.vertices = v
    
    def getGraph(self):
        return self.graph
    
    def addEdge(self, u: int, v: int) -> None:
        self.graph[u].append(v)
    
    def BFS(self, root: int) -> None:
        visited = [False] * self.vertices
        queue = []
        queue.append(root)
        visited[root] = True

        while queue:
            node = queue.pop(0)
            print(node, end=" ")
            for child in self.graph[node]:
                if not visited[child]:
                    queue.append(child)
                    visited[child] = True
    
    def DFS(self, root: int) -> None:
        visited = [False] * self.vertices
        stack = []
        visited[root] = True
        stack.append(root)
        while stack:
            node = stack.pop()
            print(node, end=" ")
            
            for child in self.graph[node]:
                if not visited[child]:
                    stack.append(child)
                    visited[child] = True

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v,end=" ")
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
 
    def DFS2(self):
        visited = set()
        for vertex in self.graph:
            if vertex not in visited:
                self.DFSUtil(vertex, visited)


    # used to print topological sort of DAG (directed acyclic graph)
    # check it is having issue
    def kahn(self):
        indeg = [0]*self.vertices
        for i in self.graph:
            for j in self.graph[i]:
                indeg[j] += 1
        queue = []
        for i in range(self.vertices):
            if indeg[i]==0:
                queue.append(i)
        cnt = 0
        ans = []
        while queue:
            u = queue.pop(0)
            ans.append(u)
            for i in self.graph[u]:
                indeg[i] -= 1
                if indeg[i] == 0:
                    queue.append(i)
            cnt += 1
        if cnt != self.vertices:
            # print("there is cycle in graph")
            return []
        else:
            return ans

if __name__=="__main__":
    g = Graph(9)

    edges = [[1,0],[2,0],[3,1],[3,2]]

    for edge in edges:
        g.addEdge(edge[0], edge[1])
    
    # print(g.getGraph())
    # g.BFS(0)
    # print(" ")
    # g.DFS(0)
    # print(" ")
    # g.DFS2()
    print(g.kahn()) # [0,2,1,3]