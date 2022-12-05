# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def printLL(self):
#         temp = self.head
#         while(temp):
#             print(temp.data)
#             temp = temp.next
    
#     def append(head,data):

#         while head:
#             head = head.next
#         head = Node(data)
#         return head


# if __name__ == "__main__":
#     list1 = LinkedList()
#     list1.head = Node(1)
#     sec = Node(2)
#     thi = Node(3)
#     list1.head.next = sec
#     sec.next = thi
#     list1.printLL()


from collections import defaultdict
from email.policy import default
from itsdangerous import NoneAlgorithm
import sys

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
    def deleteNode(self, root, key):
        if not root:
            return None
        if key == root.info:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            if root.left and root.right:
                temp = root.right
                while temp.left:
                    temp = temp.left
                root.info = temp.info
                root.right = self.deleteNode(root.right, root.info)
        elif key < root.info:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
    
    def floorNode(root: Node, key: int) -> int:
        ans = sys.maxsize + 1
        while root:
            if root.info == key:
                return key
            elif root.info > key:
                root = root.left
            else:
                ans = root.info
                root = root.right
        return ans
    
    def ceilNode(root: Node, key: int) -> int:
        ans = -sys.maxsize - 1
        while root:
            if root.info == key:
                return key
            elif root.info < key:
                root = root.right
            else:
                ans = root.info
                root = root.left
        return ans
    
    

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
# Preorder = Root, Left, Right
# preorder means DFS
def preOrder(root):
    if root:
        print(root.info, end=" ")
        preOrder(root.left)
        preOrder(root.right)

# Postorder = Left, Right, Root
def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.info, end=" ")

# Inorder = Left, Root, Right
def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.info, end=" ")
        inOrder(root.right)

# Inorder without recursion
def inOrder2(root):
    cr = root
    s = []
    while True:
        if cr:
            s.append(cr)
            cr = cr.left
        elif s:
            cr = s.pop()
            print(cr.info, end=" ")
            cr = cr.right
        else:
            break

# check if a tree is bst or not
def isBST(root):
    return isBSTUtil(root, -4294967296, 4294967296)

def isBSTUtil(node, min, max):
    if not node:
        return True
    if node.info<min or node.info>max:
        return False
    return isBSTUtil(node.left, min, node.info-1) and isBSTUtil(node.right, node.info+1, max)

def isBST2(root, l=None, r=None):
    if root==None:
        return True
    if l!=None and root.info <= l.info:
        return False
    if r!=None and root.info >= r.info:
        return False
    return isBST2(root.left, l, root) and isBST2(root.right, root, r)

# calculate the height of tree (min height log n and max height n)
def height(node):
    if node is None:
        return -1  # prints max edges from root to leaf # return 0 for prints the max level including root and leaf
    return 1 + max(height(node.left), height(node.right))
    # l = height(node.left)
    # r = height(node.right)
    # return l+1 if l>r else r+1

# prints level by level nodes (also called BFS)
def levelOrder(root):
    q = [root]
    while q:
        n = q.pop(0)
        print(n.info, end=" ")
        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)

def DFS(root):
    s = [root]
    while s:
        n = s.pop()
        print(n.info, end=" ")
        if n.left:
            s.append(n.left)
        if n.right:
            s.append(n.right)

def search(root, key):
    if root is None or root.info==key:
        return root
    if key<root.info:
        return search(root.left, key)
    return search(root.right, key)


def minValNode(node):
    cur = node
    while cur.left:
        cur = cur.left
    return cur

def deleteNode(root, key):
    if root is None:
        return root
    
    if key<root.info:
        root.left = deleteNode(root.left, key)
        return root
    elif key>root.info:
        root.right = deleteNode(root.right, key)
        return root
    
    # if root is a leaf node
    if root.left is None and root.right is None:
        return None
    
    # if root has right child only
    if root.left is None:
        temp = root.right
        root = None
        return temp
    # if root has left child only
    elif root.right is None:
        temp = root.left
        root = None
        return temp
    
    # if root has both childs
    succParent = root
    succ = root.right
    while succ.left:
        succParent = succ
        succ = succ.left
    
    if succParent != root:
        succParent.left = succ.right
    else:
        succParent.right = succ.right
    root.info = succ.info
    return root

def deleteTree(root):
    if root is None:
        return None
    q = [root]
    temp = None
    while q:
        temp = q.pop(0)
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
        del temp
    root = None

def reverseInorder(root):
    if root:
        reverseInorder(root.right)
        print(root.info, end=" ")
        reverseInorder(root.left)

def ancestors(root, target):
    if not root:
        return False
    if root.info == target:
        return True
    if ancestors(root.left, target) or ancestors(root.right, target):
        print(root.info, end=" ")
        return True
    return False

# lowest common ancestors in binary tree
def lowestCommonAncestor(self, root: Node, p: Node, q: Node) -> Node:
    if root is None:
        return None
    if root.val == p.val or root.val == q.val:
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if left is None:
        return right
    if right is None:
        return left
    return root

from typing import List
def printLeaves(root: Node) -> List[List[int]]:
    res = defaultdict(list)
    leaves(root, res)
    return list(res.values())

def leaves(root: Node, res: List[List[int]]) -> int:
    if not root:
        return -1
    le = leaves(root.left, res)
    ri = leaves(root.right, res)
    height = max(le, ri) + 1
    res[height].append(root.info)
    return height

# t = int(input())
# arr = list(map(int, input().split()))
tree = BinarySearchTree()
t = 8
arr = [6, 3, 4, 9, 7, 1, 8, 2]
for i in range(t):
    tree.create(arr[i])
print(printLeaves(tree.root))

# key = 3
ancestors(tree.root, 8)
# result = search(tree.root, key)
# if result is None:
#     print(key, "not found")
# else:
#     print(key, "found")
# print("height:", height(tree.root))

# # # # # # # #
#       6     #
#     /   \   #
#    3     9  #
#   / \   /   #
#  1   4  7   #
#   \      \  #
#    2      8 #
# # # # # # # #


# print(reverseInorder(tree.root))

# levelOrder(tree.root) # 6 3 9 1 4 7 2 8 same as BFS
# print("")
# preOrder(tree.root)
# print("")
# DFS(tree.root)
# print("")
# DFS(tree.root)
# uses a stack can be of any order we can either go left first then right or right first then left
# inorder, preorder and postorder traversal are types of dfs
# to delete a tree completely, use postorder traversal, and instead of printing, just set node = None
# postorder is used because we will delete leaf nodes first otherwise if we delete root first we can't access the child nodes

# print(search(tree.root, 4)) #True
# print(search(tree.root, 5)) #False

# print("tree inorder =", end=" ")
# inOrder(tree.root)
# a = tree.deleteNode(tree.root, 3)
# tree.deleteNode(tree.root, 3)
# tree.deleteNode(tree.root, 9)
# deleteTree(tree.root)
# deleteNode(tree.root, 3)
# deleteNode(tree.root, 5)
# print("\nafter delete =",end=" ")
# print('')
# inOrder(tree.root)

# print("pre", end=" ")
# preOrder(tree.root)
# print("\nin", end=" ")
# inOrder(tree.root)
# print("\npost", end=" ")
# postOrder(tree.root)
# inorder also prints a tree node values in ascending order
# print("\nheight", height(tree.root))
# print("\nin2",end=" ")
# inOrder2(tree.root)

# if isBST(tree.root):
# if isBST2(tree.root):
#     print("YES")
# else:
#     print("NO")
