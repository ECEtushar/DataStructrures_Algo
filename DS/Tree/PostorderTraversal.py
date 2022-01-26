from sample_tree import root

def Postorder(root):
    if root!=None:
        Postorder(root.left)
        Postorder(root.right)
        print(root.k,end=' ')


Postorder(root)