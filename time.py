
from typing import List
def timeMap(city: List[List[int]]) -> int:
    start = city[0][0]
    for i in range(len(city)-1, -1, -1):
        for j in range(len(city[0]), -1, -1):
            if i-1 > 1 and j-1 > 1:
                up = max(city[i][j], city[i-1][j])
                left = max(city[i][j], city[i][j-1])
                city[i][j] = min(up, left)
    return city[0][0] + start
# print(timeMap([[1, 2, 1], [2, 3, 2], [0, 1, 2]]))
print(timeMap([[3, 3, 1], [2, 8, 1]]))


