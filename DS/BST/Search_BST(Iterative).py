from BST import root,Traversal
from collections import deque

def serBST(root,x):
    if root is None:
        return False
    curr=root
    while curr!=None:
        if curr.k==x:
            return True
        elif curr.k>x:
            curr=curr.left
        else:
            curr=curr.right
    return False
tree=Traversal()
tree.levelOrder(root)
print(serBST(root,60))

