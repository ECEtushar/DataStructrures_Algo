from itsdangerous import NoneAlgorithm
from BST import root, Traversal,BST

def Insert(root,x):
    if root==None:
        return BST(x)
    curr=root
    while curr:
        parent=curr
        if curr.k==x:
            return
        elif curr.k>x:
            curr=curr.left
        elif curr.k<x:
            curr=curr.right
    if parent.k>x:
        parent.left=BST(x)
    else:
        parent.right=BST(x)
    return root

tree=Traversal()
tree.preorder(root)
print('\n')

root=Insert(root,45)
tree.preorder(root)

    
