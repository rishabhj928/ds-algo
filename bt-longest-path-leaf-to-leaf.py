# Python3 program to print the longest
# leaf to leaf path
 
# Tree node structure used in the program
class Node:
     
    def __init__(self, x):
         
        self.data = x
        self.left = None
        self.right = None
 
# Function to find height of a tree
def height(root):
      
    global ans, k, lh, rh, f
     
    if (root == None):
        return 0
 
    left_height = height(root.left)
 
    right_height = height(root.right)
 
    # Update the answer, because diameter of a
    # tree is nothing but maximum value of
    # (left_height + right_height + 1) for each node
    if (ans < 1 + left_height + right_height):
        ans = 1 + left_height + right_height
 
        # Save the root, this will help us finding the
        # left and the right part of the diameter
        k = root
 
        # Save the height of left & right
        # subtree as well.
        lh = left_height
        rh = right_height
 
    return 1 + max(left_height, right_height)
 
# Prints the root to leaf path
def printArray(ints, lenn, f):
     
    # Print left part of the path
    # in reverse order
    if (f == 0):
        for i in range(lenn - 1, -1, -1):
            print(ints[i], end = " ")
 
    # Print right part of the path
    elif (f == 1):
        for i in range(lenn):
            print(ints[i], end = " ")
 
# This function finds out all the
# root to leaf paths
def printPathsRecur(node, path, maxm, pathlen):
     
    global f
 
    if (node == None):
        return
 
    # Append this node to the path array
    path[pathlen] = node.data
    pathlen += 1
 
    # If it's a leaf, so print the
    # path that led to here
    if (node.left == None and node.right == None):
         
        # Print only one path which is equal to the
        # height of the tree.
        # print(pathlen,"---",maxm)
        if (pathlen == maxm and (f == 0 or f == 1)):
             
            # print("innn")
            printArray(path, pathlen,f)
            f = 2
 
    else:
         
        # Otherwise try both subtrees
        printPathsRecur(node.left, path, maxm, pathlen)
        printPathsRecur(node.right, path, maxm, pathlen)
 
# Computes the diameter of a binary
# tree with given root.
def diameter(root):
     
    global ans, lh, rh, f, k, pathLen
 
    if (root == None):
        return
     
    # f is a flag whose value helps in printing
    # left & right part of the diameter only once
    height_of_tree = height(root)
    lPath = [0 for i in range(100)]
 
    # print(lh,"--",rh)
 
    # Print the left part of the diameter
    printPathsRecur(k.left, lPath, lh, 0)
    print(k.data, end = " ")
    rPath = [0 for i in range(100)]
    f = 1
 
    # Print the right part of the diameter
    printPathsRecur(k.right, rPath, rh, 0)

def height2(root: Node) -> int:
    if root is None:
        return 0
    return 1 + max(height2(root.left), height2(root.right))

def diameter2(root: Node):
    if root is None:
        return 0
    dl = diameter2(root.left)
    dr = diameter2(root.right)
    cur = height2(root.left) + height2(root.right) + 1
    return max(cur, dl, dr)

# Driver code
if __name__ == '__main__':
     
    k, lh, rh, f, ans, pathLen = None, 0, 0, 0, 0 - 10 ** 19, 0
     
    # Enter the binary tree ...
    #          1
    #        /   \
    #       2     3
    #     /   \    \
    #    4     5    0
    #     \   / \
    #      8 6   7
    #     /
    #    9
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.right = Node(0)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.left = Node(6)
    root.left.right.right = Node(7)
    root.left.left.right = Node(8)
    root.left.left.right.left = Node(9)
 
    diameter(root)
    print("")
    print(diameter2(root))