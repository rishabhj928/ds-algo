
from typing import List
import heapq

def solve(A: List[int]) -> int:
    if not A or len(A) == 0:
        return 0
    
    h = []
    heapq.heapify(A)

    while len(A) > 1:
        x = heapq.heappop(A)
        y = heapq.heappop(A)
        print(x, y)
        heapq.heappush(A, x + y)
    return A

print(solve([4,3,2,6]))