class Node:
	def __init__(self, data: int) -> None:
		self.data = data
		self.left = self.right = None
class BinarySearchTree:
	def __init__(self):
		self.root = None
	def addNode(self, data: int) -> None:
		if self.root is None:
			self.root = Node(data)
		current = self.root
		while True:
			if data < current.data:
				if current.left:
					current = current.left
				else:
					current.left = Node(data)
					break
			elif data > current.data:
				if current.right:
					current = current.right
				else:
					current.right = Node(data)
					break
			else:
				break
	def searchNode(self, root: Node, key: int) -> Node:
		if root is None or root.data == key:
			return root
		if key < root.data:
			return self.searchNode(root.left, key)
		return self.searchNode(root.right, key)
	def getHeight(self, root: Node) -> int:
		if root is None:
			return -1
		return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
	def preOrder(self, root: Node) -> None:
		if root:
			print(root.data, end=" ")
			self.preOrder(root.left)
			self.preOrder(root.right)
	def inOrder(self, root: Node) -> None:
		if root:
			self.inOrder(root.left)
			print(root.data, end=" ")
			self.inOrder(root.right)
	def postOrder(self, root: Node) -> None:
		if root:
			self.postOrder(root.left)
			self.postOrder(root.right)
			print(root.data, end=" ")

if __name__ == "__main__":
	bst = BinarySearchTree()
	nodes = [5,7,3,6,1,8,4,9,2]
	for node in nodes:
		bst.addNode(node)
	
	print("Height:", bst.getHeight(bst.root))
	print("Search 3:", bst.searchNode(bst.root, 3))
	print("Search 0:", bst.searchNode(bst.root, 0))
	print("Pre:",end=" ")
	bst.preOrder(bst.root)
	print("\nIn:",end=" ")
	bst.inOrder(bst.root)
	print("\nPost:",end=" ")
	bst.postOrder(bst.root)
