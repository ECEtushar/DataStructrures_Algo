class Tree:
    def __init__(self, k):
        self.data = k
        self.left = None
        self.right = None


root = Tree(1)  # Root of tree
root.left = Tree(2)  # Left child of root 10
root.right = Tree(3)  # Left child of root 20
root.left.left = Tree(4)
root.left.right = Tree(5)
root.left.right.left = Tree(6)
root.left.right.right = Tree(7)
def show_tree():
    tree = """
              1
            /    \  
           2       3
         /   \       \n
       4      5 
             /  \\
            6    7
                 

    """
    print(tree)