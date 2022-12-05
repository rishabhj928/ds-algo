
from typing import List
class Node:
    def __init__(self, data: int) -> None:
        self.left = None
        self.right = None
        self.data = data

def topView(root: Node) -> None:
    pass

def bottomView(root: Node) -> None:
    pass


def leftView(root: Node) -> None:
    result = [None] * 7 # 7 here is no of nodes
    leftViewUtil(root, result, 0)
    for node in result:
        if node is None:
            break
        print(node.data, end=" ")

def leftViewUtil(root: Node, result: List[Node], level: int) -> Node:
    if root is None:
        return
    if result[level] is None:
        result[level] = root
    leftViewUtil(root.left, result, level + 1)
    leftViewUtil(root.right, result, level + 1)

def rightView(root: Node) -> None:
    result = [None] * 7 # no of nodes
    rightViewUtil(root, result, 0)
    for node in result:
        if node is None:
            break
        print(node.data, end=" ")

def rightViewUtil(root: Node, result: List[Node], level: int) -> Node:
    if root is None:
        return
    result[level] = root
    rightViewUtil(root.left, result, level + 1)
    rightViewUtil(root.right, result, level + 1)

tree = Node(4)
tree.left = Node(7)
tree.right = Node(6)
tree.right.right = Node(2)
tree.right.right.left = Node(5)
tree.right.right.right = Node(1)
tree.right.right.right.left = Node(3)

leftView(tree)
print("")
rightView(tree)
topView(tree)
bottomView(tree)
