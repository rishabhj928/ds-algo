
# Min cost to connect all points
# Given a list of 2d point coordinates, return the min cost to connect all nodes
# the cost to connect two points (x1, y1) and (x2, y2) = abs(x2-x1) + abs(y2-y1) (manhattan distance)
 
# Hint: construct all combinations of points as edges of a graph with weight as manhattan distance
# Make min spanning tree and return it's cost

from typing import List
class Graph:
    def __init__(self, vertices: int) -> None:
        self.vertices = vertices
        self.graph = []
    
    def addEdge(self, x: int, y: int, w: int) -> None:
        self.graph.append([x, y, w])

    def find(self, parent: List[int], i) -> int:
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
    
    def union(self, parent: List[int], rank: List[int], x: int, y: int) -> None:
        xp = self.find(parent, x)
        yp = self.find(parent, y)
        if rank[xp] < rank[yp]:
            parent[xp] = yp
        elif rank[xp] > rank[yp]:
            parent[yp] = xp
        else:
            parent[yp] = xp
            rank[xp] += 1
    
    def kruskal(self) -> int:
        cost, i, e, parent, rank = 0, 0, 0, [], []
        self.graph = sorted(self.graph, key=lambda item:item[2])
        mst = []
        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)
        while e < self.vertices-1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x!=y:
                e += 1
                mst.append([u, v, w])
                self.union(parent, rank, x, y)
        for u, v, w in mst:
            cost += w
            print(u, " - ", v, "cost =", w)
        return cost

    # modify this
    # def isCyclic(self):
    #     parent = [-1]*(self.V)
    #     for i in self.graph:
    #         for j in self.graph[i]:
    #             x = self.find_parent(parent, i)
    #             y = self.find_parent(parent, j)
    #             if x == y:
    #                 return True
    #             self.union(parent,x,y)

if __name__=="__main__":
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]] #20
    # points = [[3,12],[-2,5],[-4,1]] #18
    vertices = len(points)
    g = Graph(vertices)
    for i in range(vertices):
        for j in range(i+1, vertices):
            cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            g.addEdge(i, j, cost)
    cost = g.kruskal()
    print(cost)

