
import math
from collections import defaultdict

def minimumPouringWaterPenalty(parent, water, oh, uh):
    adj = defaultdict(list)
    for i in range(len(parent)):
        adj[parent[i]].append(i)
    
    water_level = [[-1 for _ in range(2)] for _ in range(len(parent))]
    
    def dfs(node, water_level, water, adj):
        stack = [[node, [0,0]]]

        while stack:
            curnode, penalty = stack.pop()
            nodePenalty = [0, 0] # oh, uh
            if water[curnode] == 1: 
                nodePenalty[0] += 1
            if water[curnode] == -1:
                nodePenalty[1] += 1
            
            if water_level[curnode][0] != -1:
                penalty = water_level[curnode]
            
            if curnode in adj:
                for child in adj[curnode]:
                    stack.append([child, penalty])
                    nodePenalty[0] += penalty[0]
                    nodePenalty[1] += penalty[1]
            
            water_level[curnode] = nodePenalty
            return water_level[curnode]
        
    dfs(0, water_level, water, adj)

    
    if_no_water = water_level[0][1] * uh
    global_min = math.inf
    for i in range(len(parent)):
        global_min = min(global_min, (if_no_water - water_level[i][1] * uh + water_level[i][0] * oh))
    return global_min
        

if __name__ == '__main__':
    print(minimumPouringWaterPenalty([-1, 0, 1], [0, 1, -1], 3, 5) == 0)
    print(minimumPouringWaterPenalty([-1, 0, 1], [-1, -1, -1], 3, 5) == 0)
    print(minimumPouringWaterPenalty([-1, 0, 0], [1, -1, -1], 10, 15) == 10)
    print(minimumPouringWaterPenalty([-1, 0, 0, 1], [0, 0, 0, 0], 10, 15) == 0)
    print(minimumPouringWaterPenalty([-1, 0, 1, 0, 1, 2, 2, 2, 5, 5], [-1, -1, 0, -1, 0, 0, 1, 0, 0, 1], 2, 3) == 4)
