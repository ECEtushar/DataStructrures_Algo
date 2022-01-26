from sample_tree import root

def maxOfTree(root):
    if root==None:
        return 0
    final = max(maxOfTree(root.left),root.k,maxOfTree(root.right))
    return final


print(maxOfTree(root))
