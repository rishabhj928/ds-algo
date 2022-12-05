from typing import List
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None

class NumArray:
    def __init__(self, nums: List[int]):
        self.root = self.createTree(nums, 0, len(nums)-1)

    def createTree(self, arr, start, end):
        if start > end:
            return None
        if start == end:
            n = Node(start, end)
            n.total = arr[start]
            return n
        mid = (start + end) // 2
        root = Node(start, end)
        root.left = self.createTree(arr, start, mid)
        root.right = self.createTree(arr, mid+1, end)
        root.total = root.left.total + root.right.total
        return root
    
    def update(self, index: int, val: int) -> None:
        return self.updateTree(self.root, index, val)
    
    def updateTree(self, root, index, value):
        if root.start == root.end:
            root.total = value
            return value
        mid = (root.start + root.end) // 2
        if index <= mid:
            self.updateTree(root.left, index, value)
        else:
            self.updateTree(root.right, index, value)
        root.total = root.left.total + root.right.total
        return root.total

    def sumRange(self, left: int, right: int) -> int:
        return self.sumTree(self.root, left, right)
    
    def sumTree(self, root, i, j):
        if root.start == i and root.end == j:
            return root.total
        mid = (root.start + root.end) // 2
        if j <= mid:
            return self.sumTree(root.left, i, j)
        elif i >= mid+1:
            return self.sumTree(root.right, i, j)
        else:
            return self.sumTree(root.left, i, mid) + self.sumTree(root.right, mid+1, j)

obj = NumArray([1,3,5])
print(obj.sumRange(0, 2))
obj.update(1, 2)
print(obj.sumRange(0, 2))