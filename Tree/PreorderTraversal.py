from Tree import root

def preorder(root):
    if root == None:
        return

    print(root.data,end=',')
    preorder(root.left)
    preorder(root.right)


if __name__ == "__main__":
    preorder(root)