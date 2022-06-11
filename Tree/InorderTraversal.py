from sample_tree import root


def Inorder(root):
    if root!=None:
        Inorder(root.left)
        print(root.k,end=' ')
        Inorder(root.right)

Inorder(root)