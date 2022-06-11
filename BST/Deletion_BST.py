import re
from tkinter.messagebox import NO
from BST import root,Traversal

def getSucc(root):
    curr=root
    while curr.left!=None:
        curr=curr.left
    return curr.k

def Del_BST(root,x):
    if root==None:
        return
    if x<root.k:
        root.left=Del_BST(root.left,x)
    elif x>root.k:
        root.right=Del_BST(root.right,x)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        else:
            succ=getSucc(root.right)
            root.k=succ
            root.right=Del_BST(root.right,succ)
    return root

tree=Traversal()
temp=root
tree.preorder(temp)
print('\n')
Del_BST(temp,50)
tree.preorder(temp)

