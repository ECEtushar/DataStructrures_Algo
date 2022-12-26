from Tree import root

def treeSize(root):
    if root==None:
        return 0
    else:
        return (treeSize(root.left)+treeSize(root.right)+1)

sz=treeSize(root)
print(sz)