from collections import defaultdict
class Tree:
    def __init__(self) -> None:
        self.tree = defaultdict(list)
    def addVertice(self, x: int, y: int) -> None:
        self.tree[x].append(y)
    def inOrder(self, root: int) -> None:
        if root:
            print(root)
            for kid in self.tree[root]:
                self.inOrder(kid)

if __name__ == "__main__":
    tree = Tree()
    vert = [[1,2], [1,3], [2,4], [2,5], [3,6], [3,7]]
    for v in vert:
        tree.addVertice(v[0],v[1])
    tree.inOrder(1)