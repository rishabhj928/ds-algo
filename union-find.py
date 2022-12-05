# Union Find: This code is used to detect a cycle in an undirected graph
import time
start = time.time()
from collections import defaultdict
from typing import List
class Graph:
    def __init__(self, vertices: int) -> None:
        self.vertices = vertices
        self.graph = defaultdict(list)
    
    def addEdge(self, x: int, y: int) -> None:
        self.graph[x].append(y)
    
    def find_parent(self, parent: List[int], i: int) -> int:
        if parent[i] == -1:
            return i
        return self.find_parent(parent, parent[i])
    
    def union(self, parent: List[int], rank: List[int], x: int, y: int) -> None:
        # parent[x] = y
        xroot = self.find_parent(parent, x)
        yroot = self.find_parent(parent, y)
        if rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        elif rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
    
    def detectCycle(self) -> bool:
        parent = [-1] * self.vertices
        rank = [0] * self.vertices
        for vertice in self.graph:
            for adj in self.graph[vertice]:
                x = self.find_parent(parent, vertice)
                y = self.find_parent(parent, adj)
                # print("->",x,y)
                if x == y:
                    return True
                self.union(parent, rank, x, y)

    def DFS(self, node:int, visited:set) -> None:
        if node not in visited:
            visited.add(node)
            print(node, end=" ")
            for adj in self.graph[node]:
                self.DFS(adj, visited)
    def pp(self):
        return self.graph

if __name__ == "__main__":
    g = Graph(9)
    edges = [[1,2],[3,4],[5,6],[7,8],[2,4],[2,5],[1,3],[6,8]]
    for e in edges:
        g.addEdge(e[0],e[1])
    print(g.detectCycle())
    g.DFS(1,set())
    # print(g.pp())
    print(time.time() - start)
