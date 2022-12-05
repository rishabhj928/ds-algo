
# Q1 You are given a string S of length N, Q ranges of the form [L, R] in a 2D array range, 
# and a permutation arr containing numbers from 1 to N.

# In one permutation, you remove the first unremoved character as per the permutation.
# However, the positions of the other characters will not change. Determine the minimum
# number of operations for the remaining string to be good.

# Notes:
# - A string is considered good if all the Q ranges have all distinct characters. Removed chars are not counted.
# - A range with all chars removed is considered to have all distinct chars.
# - The sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.
# - 1-based indexing is followed

# e.g.
# N = 5, Q = 2, S = 'aaaaa'
# arr = [2, 4, 1, 3, 5]
# ranges = [[1, 2], [4, 5]]

# after first permutation arr[0] - s = a_aaa
# 2nd - s = a_a_a
# now in both the ranges [(1,2) and (4,5)], all chars are distinct, hence output is 2

# N = 8, Q = 3, S = 'abbabaab'
# arr = [6, 3, 5, 1, 4, 2, 7, 8]
# ranges = [[1, 3], [4, 7], [3, 5]]

# 1 - abbab_ab
# 2 - ab_ab_ab
# 3 - ab_a__ab
# 4 - _b_a__ab
# 5 - _b____ab
# now in all ranges, all chars are distinct, hence output is 5


"""
from typing import List

def isDistinctRange(s: List[str], ranges: List[List[int]]) -> bool:
    for i in range(len(ranges)):
        l, r = ranges[i]
        s2 = []
        for j in range(l-1, r):
            if s[j] != '_':
                s2.append(s[j])
        if len(set(s2)) != len(s2):
            return False
    return True

def goodString(N: int, Q: int, S: str, arr: List[int], ranges: List[List[int]]) -> int:
    s = list(S)
    if isDistinctRange(s, ranges):
        return 0
    for i in range(len(arr)):
        s[arr[i] - 1] = '_'
        if isDistinctRange(s, ranges):
            return i + 1

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N, Q = map(int, input().split(" "))  # N = length of S, Q = no of ranges
        S = input() # string
        arr = list(map(int, input().split(" "))) # permutation array
        ranges = []
        for q in range(Q):
            ranges.append(list(map(int, input().split(" "))))
        print(goodString(N, Q, S, arr, ranges))
"""

# Q2 There are N provinces [1, 2, ..., N]. King Bob wants to create his kingdom. For this, he needs to capture some provinces.
# two provinces can be connected by water, land, or by both. A pair of provinces are connected by land and B pairs of provinces 
# are connected by water. Since bob's navy is very weak, he does not want any of his captured provinces to be connected by water,
# moreover, Bob has a strong army, so he wants to capture every province that is connected to his kingdom by land.
# 
# For each captured province every province connected to it by land should also be captured.
# No two provinces captured should be connected by water directly or by any other provinces.
# Any two captured provinces should be connected directly or through other captured provinces.
# 
# Output the max no of provinces that Bob can capture, if not possible, return 0
# 
# N = 5, A = 2, B = 1
# land = [[1, 2], [2, 3]]
# water = [[1, 3]]
# 
# province 1 is connected to 2 by land, 1 is connected to 3 by water, 2-3 by land
# 4, 5 provinces can be captured
# 1, 2, 3 can't be captured bacause 1 and 3 are connected by water
# so ans is 1 [4], [5]
# 
# N = 5, A = 2, B = 1
# land = [[1, 2]]
# water = [[1, 3], [3, 2]]
# 
# 1 and 2 are connected by land, 1 and 3 are connected by water, 3 and 2 also by water
# max group of provinces connected by land is two, [1, 2] since 1 is connected to 3 by water, 
# 3 is connected to 2 by water, so 1 and 2 are indirectly connected to water, so we can't take this group
# therefore the max no of provinces captured is 1 [3], [4], [5]


"""
graph has N elements, from 1 to N
A = land edges
B = water edges
to find max size of graph cycle components by land only
Approach
1. Construct a directed graph for land only, and ignore water
2. Consider a single node as cycle, as it can be captured
3. Detect cycle in graph, find it's size/no of nodes, and return max of all those
"""
from typing import List
from collections import Counter
def find(parent, i):
    if parent[i] == i:
        return i
    parent[i] = find(parent, parent[i])
    return parent[i]

def captureProvinces(N: int, A: int, B: int, land: List[List[int]], water: List[List[int]]) -> int:
    l = list(range(N+1))
    w = list(range(N+1))
    for i, j in land:
        l[find(l, i)] = l[find(l, j)]
    for i, j in water:
        w[find(w, i)] = w[find(w, j)]
    visit = [[0]*(N+1) for _ in range(N+1)]
    ct = Counter(find(l, i) for i in range(1, N+1))
    for i in range(N+1):
        i = find(l, i)
        j = find(w, i)
        visit[i][j] += 1
        if visit[i][j] > 1:
            ct[i] = 0
    return max(ct.values())
    

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N = int(input()) # no of provinces
        A = int(input()) # no of pairs of land
        B = int(input()) # no of pairs of water
        land = []
        water = []
        for a in range(A):
            land.append(list(map(int, input().split(" "))))
        for b in range(B):
            water.append(list(map(int, input().split(" "))))
        print(captureProvinces(N, A, B, land, water))

