from sample_tree import root


def Preorder(root):

    if root!=None:
        print(root.k,end=' ')
        Preorder(root.left)
        Preorder(root.right)


Preorder(root)
