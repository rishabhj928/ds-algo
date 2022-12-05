
#User function Template for python3





from collections import defaultdict

class Pair:
    def __init__(self, node, cost):
        self.node = node
        self.cost = cost

class Solution:
    def solve(self, N, Q, Edge, query):
        graph = defaultdict(set)
        for u, v in Edge:
            graph[u].add(v)
            graph[v].add(u)
        ans = []
        
        for x, y in query:
            graph[x].discard(y)
            graph[y].discard(x)
            mx = 0
            stack = [Pair(0, 0)]
            visited = {0}
            while stack:
                p = stack.pop()
                cur = p.node
                cost = p.cost
                mx = max(mx, cost)
                for adj in graph[cur]:
                    if adj not in visited:
                        visited.add(adj)
                        stack.append(Pair(adj, cost + 1))
            ans.append(mx)
            graph[x].add(y)
            graph[y].add(x)
        return ans

for _ in range (int(input())):
    n , q = [int(i) for i in input().split()]
    edge = []
    for i in range (n-1):
        edge.append([int(i) for i in input().split()])
    query = []
    for i in range (q):
        query.append([int(i) for i in input().split()])
    sol = Solution()
    ans = sol.solve(n, q, edge, query)
    for i in ans:
        print(i, end=" ")
    print()
