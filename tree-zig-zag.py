# Given a binary tree, print its zig zag traversal level by level
# level 0 - ltr, level 1 - rtl and so on


from typing import List
from collections import deque
class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None

def buildTree(arr, i: int, n: int) -> Node:
    root = None
    if i < n:
        if arr[i] == None:
            return
        root = Node(arr[i])
        root.left = buildTree(arr, 2*i+1, n)
        root.right = buildTree(arr, 2*i+2, n)
    return root

def inorder(root: Node) -> None:
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def zigzag(root: Node) -> List[int]:
    dq = deque([root])
    ans = []
    flip = 1
    while dq:
        level = []
        for i in range(len(dq)):
            node = dq.popleft()
            level.append(node.data)
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
        ans.append(level[::flip])
        flip *= -1
    return ans

arr = [3, 9, 20, None, None, 15, 7]
root = buildTree(arr, 0, len(arr))
# inorder(root)
print(zigzag(root))
# [[3], [20, 9], [15, 7]]

#     3 
#    / \
#   9   20
#      /  \
#     15   7
