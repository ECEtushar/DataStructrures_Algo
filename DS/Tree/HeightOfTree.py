from sample_tree import root

def treeHeight(root):
    if root == None:
        return 0
    ret = max(treeHeight(root.left), treeHeight(root.right))
    return ret+1


print('Height of the tree is: ',treeHeight(root))