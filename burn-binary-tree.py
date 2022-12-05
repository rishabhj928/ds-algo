
'''
    Time Complexity: O(N)
    Space Complexity: O(N)

    where N is the total number of nodes in the given tree.
'''
from sys import stdin, setrecursionlimit
from queue import Queue
from collections import deque
from collections import defaultdict
setrecursionlimit(10**7)

class BinaryTreeNode :
	def __init__(self, data) :
		self.data = data
		self.left = None
		self.right = None

def inorder(root, graph):
    if root:
        inorder(root.left, graph)
        if root.left:
            graph[root.data].append(root.left.data)
            graph[root.left.data].append(root.data)
        if root.right:
            graph[root.data].append(root.right.data)
            graph[root.right.data].append(root.data)
        inorder(root.right, graph)

def timeToBurnTree(root, start):
    graph = defaultdict(list)
    inorder(root, graph)
    dq = deque([start])
    count = 0
    visited = set(start)
    
    while dq:
        count += 1
        for i in range(len(dq)):
            node = dq.popleft()
            for adj in graph[node]:
                if adj not in visited:
                    dq.append(adj)
                    visited.add(adj)
    return count - 1

# Fast input
def takeInput() :
	
    arr = list(map(int, stdin.readline().strip().split(" ")))

    rootData = arr[0]

    n = len(arr)

    if(rootData == -1) :
        start = int(input().strip())
        return None, start

    root = BinaryTreeNode(rootData)
    q = Queue()
    q.put(root)
    index = 1
    while(q.qsize() > 0) :
        currentNode = q.get()  
        
        leftChild = arr[index]
        
        if(leftChild != -1) :
            leftNode =  BinaryTreeNode(leftChild)  
            currentNode.left = leftNode  
            q.put(leftNode)  
        
        index += 1
        rightChild = arr[index]
        
        if(rightChild != -1) :
            rightNode = BinaryTreeNode(rightChild)
            currentNode .right = rightNode  
            q.put(rightNode)  

        index += 1

    start = int(input().strip())

    return root, start

#main

root, start = takeInput()

print(timeToBurnTree(root, start))
