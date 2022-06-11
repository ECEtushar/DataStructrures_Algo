from BST import root,Traversal

def SerBST(root,x):
    if root is None:
        return False
    if root.k == x:
        return True
    else:
        if root.k > x:
            return SerBST(root.left, x)
        if root.k < x:
            return SerBST(root.right, x)

tree=Traversal()
tree.preorder(root)
print('\n')
print(SerBST(root,1000))