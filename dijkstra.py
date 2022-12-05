
# Given a weighted directed graph, and source node, find min time to traverse all nodes
# Dijkstra's Algorithm

# Time O(N + ElogN) Space O(N + E)

from collections import defaultdict
import heapq
from typing import List

class Graph:
    def __init__(self, vertices: int) -> None:
        self.vertices = vertices
        self.graph = defaultdict(list)

    def addEdge(self, x: int, y: int, w: int) -> None:
        self.graph[x].append((w, y))
    
    def dijkstra(self, start: int, n: int) -> int:
        heap = [(0, start)]
        visited = set()
        while heap:
            weight, node = heapq.heappop(heap)
            visited.add(node)
            if len(visited) == n:
                return weight   
            for wt, adj in self.graph[node]:
                if adj not in visited:
                    heapq.heappush(heap, (weight + wt, adj))
        return -1
    
if __name__ == "__main__":
    n = 4
    edges = [[2,1,1],[2,3,1],[3,4,1]]
    start = 2
    graph = Graph(n)
    for x, y, w in edges:
        graph.addEdge(x, y, w)
    print(graph.dijkstra(start, n)) #2

