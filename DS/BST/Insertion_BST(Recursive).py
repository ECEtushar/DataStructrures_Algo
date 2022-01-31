
from BST import root,Traversal,BST

def Insert(root,key):
    if root==None:
        return BST(key)
    if root.k==key:
        return root
    elif root.k>key:
        root.left=Insert(root.left,key)
    elif root.k<key:
        root.right=Insert(root.right,key)
    return root


tree=Traversal()
tree.preorder(root)
Insert(root,56)
Insert(root,65)
print('\n')
tree.preorder(root)