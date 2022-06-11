class Tree:
    def __init__(self, k):
        self.k = k
        self.left = None
        self.right = None


root = Tree(10)  # Root of tree
root.left = Tree(20)  # Left child of root 10
root.left.left = Tree(100)  # Left child of root 20
root.left.right = Tree(400)  # Right child of root 20
root.right = Tree(30)  # Right child of root 10
root.right.left = Tree(40)  # Left child of root 30
root.right.right = Tree(50)  # Right child of root 30
root.right.right.left = Tree(310) # Left child of root 50
#root.right.right.left.left = Tree(111)