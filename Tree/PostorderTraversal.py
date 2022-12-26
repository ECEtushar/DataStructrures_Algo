from Tree import root, show_tree

def postorder(root):
    if root == None:
        return
    
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=',')
    


if __name__ == "__main__":
    show_tree()
    postorder(root)