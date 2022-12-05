
from collections import defaultdict
class Graph:
	def __init__(self, vertices: int) -> None:
		self.vertices = vertices
		self.graph = defaultdict(list)
	def addEdge(self, x: int, y: int) -> None:
		self.graph[x].append(y)
	
	def DFS(self, root: int, visited = set()) -> None:
		visited.add(root)
		print(root, end=' ')
		for node in self.graph[root]:
			if node not in visited:
				self.DFS(node, visited)
g = Graph(7)
edges = [[0,1],[1,2],[1,3],[2,4],[2,5],[5,6],[2,0]]
for edge in edges:
	g.addEdge(edge[0], edge[1])
g.DFS(0, set())
