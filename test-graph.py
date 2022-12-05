from collections import defaultdict
class Graph:
	def __init__(self, vertices: int) -> None:
		self.vertices = vertices
		self.graph = defaultdict(list)
	def addEdge(self, x: int, y: int) -> None:
		self.graph[x].append(y)
		self.graph[y].append(x)
	def BFS(self, root: int) -> None:
		visited = {root}
		queue = [root]
		while queue:
			node = queue.pop(0)
			print(node, end=" ")
			for adj in self.graph[node]:
				if adj not in visited:
					visited.add(adj)
					queue.append(adj)
	def DFS(self, root: int, visited: set) -> None:
		visited.add(root)
		print(root, end=" ")
		for adj in self.graph[root]:
			if adj not in visited:
				self.DFS(adj, visited)

	# def cycleDetect(self, edges) -> None:
	# 	visited = defaultdict(list)
	# 	for i, edge in enumerate(edges):
	# 		# print(i, edge)
	# 		visited[i].append(edge[0])
	# 		visited[i].append(edge[1])

	# 	print(visited)

if __name__ == "__main__":
	myGraph = Graph(6)
	edges = [[1,2], [1,3], [2,4], [2,5], [5,6], [6,7]]
	for edge in edges:
		myGraph.addEdge(edge[0], edge[1])
	# print("BFS from 1:", end=" ")
	# myGraph.BFS(1)
	# print("\nDFS from 1:", end=" ")
	# myGraph.DFS(1, set())
	res = myGraph.cycleDetect(edges)