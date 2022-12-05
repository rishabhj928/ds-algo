global x
x = 0
def fun(x):
    return x + 1


# move all repeating elements of array to end of it
# only one element is repeated, but don't change the order of original array
# e.g. [1,5,1,10,1,2] => [5,10,2,1,1,1]
# e.g. [5,5,1,10,5,2] => [1,10,2,5,5,5]

"""
Approach: first make an empty hashmap, and then add first element to that hashmap having 1 as it's count
traverse from second element and check if it exists in that array, then increase it's count
"""
from collections import defaultdict
from time import struct_time

def shift(A):
    if not A:
        return
    hashmap = defaultdict(int)
    for i in range(len(A)):
        if A[i] not in hashmap:
            hashmap[A[i]] = 1
        else:
            hashmap[A[i]] += 1
    elem = None
    ecount = 0
    for k,v in hashmap.items():
        if v>1:
            elem=k
            ecount=v
            break
    A = list(filter((elem).__ne__, A))
    for i in range(ecount):
        A.append(elem)
    return A

def heapify(arr, n, i):
    x = i
    l = 2*i+1
    r = 2*i+2
    if l<n and arr[x]<arr[l]:
        x = l
    if r<n and arr[x]<arr[r]:
        x = r
    if x!=i:
        arr[i],arr[x] = arr[x],arr[i]
        heapify(arr, n, x)


# next greater element 1 (leetcode)
from typing import List
def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    d, st, ans = {}, [], []
    for x in nums2:
        while len(st) and st[-1] < x:
            d[st.pop()] = x
        st.append(x)
    for x in nums1:
        ans.append(d.get(x, -1))
    return ans

# Time needed to inform all employees (leetcode)
def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
    def dfs(i):
        if manager[i] != -1:
            informTime[i] += dfs(manager[i])
            manager[i] = -1
        return informTime[i]
    
    mx = -1
    for i in range(n):
        mx = max(mx, dfs(i))
    return mx
    # return max(map(dfs, range(n)))

def paintLine(points: List[List[int]]) -> List[int]:
    # low = 0
    # high = 0
    # cost = 0
    # costs = []
    # for point in points:
    #     low = point[0]
    #     high = point[1]
    #     cost = high - low
    
    mx = 0
    for x1, x2 in points:
        mx = max(mx, x2)
    mp = [False] * mx
    costs = []
    for x1, x2 in points:
        cost = 0
        for i in range(x1, x2):
            if not mp[i]:
                mp[i] = True
                cost += 1
        costs.append(cost)
    return costs
# print("paintline", paintLine([[4, 10], [7, 13], [16,20], [1, 40]])) #[6, 3, 4, 26]


def removeIslands(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix)
    m = len(matrix[0])
    matrixcopy = [[0] * m for _ in range(n)]
    visited = set()
    def dfs(i, j):
        if i < 0 or i > m - 1 or j < 0 or j > n - 1 or not matrix[i][j]:
            return
        matrixcopy[i][j] = matrix[i][j]
        if (i, j) not in visited:
            visited.add((i, j))
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                dfs(i, j)
    return matrixcopy

mt = [
        [1, 0, 0, 0, 0, 0], 
        [0, 1, 0, 1, 1, 1], 
        [0, 0, 1, 0, 1, 0], 
        [1, 1, 0, 0, 1, 0], 
        [1, 0, 1, 1, 0, 0], 
        [1, 0, 0, 0, 0, 1]
    ]
print('islands',removeIslands(mt))

# Books Allocation

def minPages(a: List[int], k: int) -> int:
    lo = min(a)
    hi = sum(a)
    res = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if isFeasible(a, k, mid):
            res = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return res

def isFeasible(a: List[int], k: int, mid: int) -> bool:
    student = 1
    sum = 0
    for i in a:
        if sum + i > mid:
            student += 1
            sum = i
        else:
            sum += i
    return student <= k

if __name__=="__main__":
    # print("minpages", minPages([10, 5, 20], 2))
    # print(x)
    # fun(x)
    # print(x)
    # arr = input("Enter space separated arr: ")
    # arr = arr.split()
    # print(shift(arr))  #[1,10,2,5,5,5]

    a = [6,3,2,4,7,9,1,5]
    n = len(a)
    for i in range(n//2+1,-1,-1):
        heapify(a, n, i)
    # print(a)
    max_so_far = 0
    prices = []
    profit = []
    l = 1
    j =1
    
    # max_so_far = max(max_so_far, prices[i] - prices[l] + profit[l][j - 1])
