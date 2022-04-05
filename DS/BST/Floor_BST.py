import re
from BST import BST,root,Traversal


def floor(root,key):
    import math
    if root is None:
        return
    if root.k==key:
        return print(key)
    curr=root
    close= -(math.inf)
    while curr!=None:
        if key>curr.k:
            close=max(close,curr.k)
            curr=curr.right
        elif key<curr.k:
            curr=curr.left
        elif curr.k==key:
            return print(key)
    if close == -(math.inf):
        return print(None)
    return print(close)

floor(root,70)


    