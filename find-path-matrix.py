
# Find if there exists a path b/w a matrix, having source = 1, destination = 2, blank cell = 3, wall = 0

from typing import List
from collections import deque
class Pair:
    def __init__(self, i, j):
        self.i = i
        self.j = j

def findPath(matrix: List[List[int]]) -> bool:
    rows = len(matrix)
    cols = len(matrix[0])
    queue = deque([])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                queue.append(Pair(i, j))
                break
    path = []
    while queue:
        cur = queue.popleft()
        i = cur.i
        j = cur.j

        # if out of bounds, do nothing, process other pairs, or if it is visited already (or it is a wall = 0), don't visit again
        if i < 0 or i >= rows or j < 0 or j >= cols or matrix[i][j] == 0:
            continue

        path.append([i, j])
        # if we reached destination (2), return True
        if matrix[i][j] == 2:
            return True
        
        # mark current cell as visited (or blocked/wall = 0)
        matrix[i][j] = 0

        # add all 4 connected cells to the queue (bfs)
        queue.append(Pair(i + 1, j))
        queue.append(Pair(i - 1, j))
        queue.append(Pair(i, j + 1))
        queue.append(Pair(i, j - 1))
    return False

matrix = [
    [ 0, 3, 0, 1 ],
    [ 3, 0, 3, 3 ],
    [ 2, 3, 3, 3 ],
    [ 0, 3, 3, 3 ]
]

print(findPath(matrix))
