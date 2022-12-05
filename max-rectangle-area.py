
# Maximum size rectangle binary sub-matrix with all 1s
# Input:
# 0 1 1 0
# 1 1 1 1
# 1 1 1 1
# 1 1 0 0
# Output: 8
# Explanation: The largest rectangle with only 1's is from (1, 0) to (2, 3) which is
# 1 1 1 1
# 1 1 1 1 
# Hint: Find max area in a histogram, for each row added to a dp array

from typing import List


def maxHistogramArea(heights: List[int]) -> int:
    heights.append(0)
    stack = [-1]
    area = 0
    for i in range(len(heights)):
        while heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            print("h =",h,"w =",w)
            area = max(area, h * w)
        stack.append(i)
    heights.pop()
    return area

# for every first row of the matrix, find histogram area, but for next occuring rows,
# sum up if it is 1 else make it 0, then find it's histogram area and calculate max among all
# Time Complexity = O(m*n)
def maxRectangle(A: List[List[int]]) -> int:
    res = maxHistogramArea(A[0])
    for i in range(1, len(A)):
        for j in range(len(A[i])):
            if A[i][j] == 1:
                A[i][j] += A[i-1][j]
        res = max(res, maxHistogramArea(A[i]))
    return res

if __name__ == "__main__":
    A = [[0, 1, 1, 0],
		[1, 1, 1, 1],
		[1, 1, 1, 1],
		[1, 1, 0, 0]]
    print(maxRectangle(A))
    