
class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None

def isLeaf(node: Node) -> int:
    if node == None:
        return 0
    if node.left == None and node.right == None:
        return 1
    return 0

def isSumTree(node: Node) -> int:
    if not node:
        return 0
    
    ls = isSumTree(node.left)
    if ls == -1:
        return -1
    
    rs = isSumTree(node.right)
    if rs == -1:
        return -1
    
    if isLeaf(node) or ls + rs == node.data:
        return ls + rs + node.data
    else:
        return -1

root = Node(26)
root.left = Node(10)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(6)
root.right.right = Node(3)
print(isSumTree(root))
