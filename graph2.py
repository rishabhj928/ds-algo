
from collections import defaultdict
class graph:
    def __init__(self, vertices: int) -> None:
        self.graph = defaultdict(list)
        self.vertices = vertices
    
    def addEdge(self, x: int, y: int) -> None:
        self.graph[x].append(y)
    def pg(self):
        return self.graph

    def BFS2(self, root: int) -> None:
        visited = [False] * (self.vertices + 1)
        queue = []
        queue.append(root)
        visited[root] = True
        while queue:
            node = queue.pop(0)
            print(node, end=" ")
            for child in self.graph[node]:
                # print("..",child)
                if not visited[child]:
                    queue.append(child)
                    visited[child] = True
    
    def DFS(self, root, visited):
        visited.add(root)
        print(root, end=" ")
        for adj in self.graph[root]:
            if adj not in visited:
                    self.DFS(adj, visited)
    
    def BFS(self, root):
        visited = set()
        queue = [root]
        visited.add(root)
        while queue:
            node = queue.pop()
            print(node, end=" ")
            for child in self.graph[root]:
                if child not in visited:
                    visited.add(child)
                    queue.append(child)

    def DFSS(self, root):
        visited = {root}
        stack = [root]
        while stack:
            node = stack.pop()
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
            for adj in self.graph(node):
                if adj not in visited:
                    stack.append(adj)

    def cycleDetect(self):
        return

    

if __name__ == "__main__":
    myGraph = graph(12)
    # edges = [[2,3], [3,4], [4,1], [1,3], [2,4],[3,2]]
    edges = [[1,20], [20,1], [1,3], [3,1], [20,4], [4,20], [20,5], [5,20], [3,6], [6,3], [3,7], [7,3]]

    for edge in edges:
        myGraph.addEdge(edge[0], edge[1])
    # myGraph.BFS(1)
    myGraph.BFS(1)
    print('')
    myGraph.DFS(1, set())
    # print(myGraph.pg())