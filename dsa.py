
# rotten oranges, 0 = empty, 1 = fresh, 2 = rotten
from typing import List
def rottenOranges(grid: List[List[int]]) -> int:
	row = len(grid)
	col = len(grid[0])
	fresh = set()
	rotten = set()
	for i in range(row):
		for j in range(col):
			if grid[i][j] == 1:
				fresh.add((i, j))
			if grid[i][j] == 2:
				rotten.add((i, j))
	time = 0
	dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
	while fresh:
		if not rotten:
			return -1
		rot = set()
		for i, j in rotten:
			for di, dj in dirs:
				if (i+di, j+dj) in fresh:
					rot.add((i+di, j+dj))
		rotten = rot
		fresh -= rotten
		time += 1
	return time

if __name__ == "__main__":
	t_c = [[[2,1,1],[1,1,0],[0,1,1]], [[2,1,1],[0,1,1],[1,0,1]], [[0,2]]]
	for t in t_c:
		print(rottenOranges(t)) # 4, -1, 0

#find single non repeating element in list of sorted twice repeated elements
def singleNonDuplicate(nums: List[int]) -> int:
	low = 0
	high = len(nums) - 1
	while low < high:
		mid = 2 * ((low + high) // 4)
		if nums[mid] == nums[mid + 1]:
			low = mid + 2
		else:
			high = mid
	return nums[low]
tc = [[1,1,2,3,3,4,4,8,8], [3,3,7,7,10,11,11]]
for t in tc:
	print(singleNonDuplicate(t)) # 2, 10


#search in an infinite sorted array whose length is not known, in logn time
def searchInfiniteSortedArray(nums: List[int], key: int) -> int:
	low = 0
	high = 1
	while nums[high] < key:
		low = high
		high = 2 * high
	while low <= high:
		mid = (low + high) // 2
		if nums[mid] == key:
			return mid
		elif nums[mid] < key:
			low = mid + 1
		else:
			high = mid - 1
	return -1
print(searchInfiniteSortedArray([1,9,2,3,8,18,92,6,7,16,4,78,19,43,81,72,93,81,72,32], 19))

#reconstruct itinerary from list of tickets given
from collections import defaultdict
def findItinerary(tickets: List[List[str]]) -> List[str]:
	graph = defaultdict(list)
	for src, des in tickets:
		graph[src].append(des)
	for src in graph:
		graph[src].sort(reverse=True)
	stack = ['JFK']
	itinerary = []
	while stack:
		while graph[stack[-1]]:
			stack.append(graph[stack[-1]].pop())
		else:
			itinerary.append(stack.pop())
	return itinerary[::-1]
tc = [[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]], [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]]
for t in tc:
	print(findItinerary(t))

#search in rotated sorted array in logn
def searchRotatedSorted(nums: List[int], key: int) -> int:
	print(nums, key)
	low = 0
	high = len(nums) - 1
	while low <= high:
		mid = (low + high) // 2
		if nums[mid] == key:
			return mid
		if nums[low] == key:
			return low
		if nums[high] == key:
			return high
		if nums[low] < nums[mid]:
			if nums[low] < key < nums[mid]:
				high = mid - 1
			else:
				low = mid + 1
		else:
			if nums[mid] < key < nums[high]:
				low = mid + 1
			else:
				high = mid - 1
	return -1
for t in [[[4,5,6,7,0,1,2], 0], [[4,5,6,7,0,1,2] , 3], [[1], 0]]:
	print(searchRotatedSorted(t[0], t[1]))

#russian doll leetcode
def maxEnvelopes(envelopes: List[List[int]]) -> int:
	envelopes.sort(key = lambda x: (x[0], -x[1]))
	heights = []
	size = 0
	for w, h in envelopes:
		if not heights or h > heights[-1]:
			heights.append(h)
			size += 1
		else:
			low, high = 0, size
			while low < high:
				mid = low + (high - low) // 2
				if heights[mid] < h:
					low = mid + 1
				else:
					high = mid
			heights[low] = h
	return size
tc = [[[5,4],[6,4],[6,7],[2,3]], [[1,1],[1,1],[1,1]]] # 3, 1
for t in tc:
	print(maxEnvelopes(t))

# Ones and Zeroes leetcode
def findMaxForm(strs: List[str], m: int, n: int) -> int:
	dp = [[0]*(n+1) for i in range(m+1)]
	for s in strs:
		ones = s.count('1')
		zeros = len(s) - ones
		for i in range(m, zeros - 1, -1):
			for j in range(n, ones - 1, -1):
				dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
	return dp[m][n]
tc = [[["10","0001","111001","1","0"], 5, 3], [["10","0","1"], 1, 1]] # 4, 2
for t in tc:
	print(findMaxForm(t[0], t[1], t[2]))

# trapping rainwater
# find maxleft and max right for current index building, get min of those and subtract current building height to get ans
def trapRainWater(heights: List[int]) -> int:
	n = len(heights)
	left = [0] * n
	right = [0] * n
	left[0] = heights[0]
	right[n-1] = heights[n-1]
	for i in range(1, n):
		left[i] = max(left[i-1], heights[i])
	for i in range(n-2, -1, -1):
		right[i] = max(right[i+1], heights[i])
	rain = 0
	for i in range(n):
		rain += min(left[i], right[i]) - heights[i]
	return rain
tc = [[0,1,0,2,1,0,1,3,2,1,2,1], [4,2,0,3,2,5]] # 6, 9
for t in tc:
	print(trapRainWater(t))

def largestRectHisto(heights: List[int]) -> int:
	if not heights or len(heights) == 0:
		return 0
	n = len(heights)
	leftSmaller = [0] * n
	rightSmaller = [0] * n
	leftSmaller[0] = -1
	rightSmaller[n-1] = n
	for i in range(1, n):
		p = i - 1
		while p >= 0 and heights[p] >= heights[i]:
			p = leftSmaller[p]
		leftSmaller[i] = p
	for i in range(n - 2, -1, -1):
		p = i + 1
		while p < n and heights[p] >= heights[i]:
			p = rightSmaller[p]
		rightSmaller[i] = p
	maxArea = 0
	for i in range(n):
		width = rightSmaller[i] - 1 - leftSmaller[i]
		curArea = width * heights[i]
		maxArea = max(maxArea, curArea)
	return maxArea
tc = [[2,1,5,6,2,3], [2,4]]  # 10, 4
for t in tc:
	print(largestRectHisto(t))

def maxRectangle(grid: List[List[int]]) -> int:
	sumArray = grid[0]
	area = largestRectHisto(sumArray)
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if grid[i][j] == 1:
				sumArray[j] += 1
			else:
				sumArray[j] = 0
		area = max(area, largestRectHisto(sumArray))
	return area
a = [[0, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 0]]
print(maxRectangle(a))  # 8


def isPalin(s: str, l: int, r: int) -> bool:
	if l >= r:
		return True
	if s[l] != s[r]:
		return False
	return isPalin(s, l + 1, r - 1)
# print(isPalin("nitin", 0, 4))

def powerSet(s: str, i: int = 0, cur: str = "", a: List[str] = []) -> List[str]:
	if i == len(s):
		a.append(cur)
		return
	powerSet(s, i+1, cur + s[i], a)
	powerSet(s, i+1, cur, a)
	return a
# print('powerset', powerSet("rishabh"))

def permute(s: str, l: int = 0, r: int = 0, a: List[str] = []) -> List[str]:
	if l == r:
		a.append(s)
		return
	for i in range(l, r+1):
		s[l], s[i] = s[i], s[l]
		permute(s, l+1, r)
		s[l], s[i] = s[i], s[l]
	return a
print('permute', permute("abc"))

