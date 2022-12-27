from Tree import root, show_tree

def inorder(root):
    if root == None:
        return

    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)

def inorder_loop(root):
    if root == None:
        return 

    curr = root
    stack = []
    res=[]
    while True:
        if curr!=None:
            stack.append(curr)
            curr = curr.left
        else:
            if stack==[]:
                break
            e = stack.pop()
            res.append(e.data)
            curr = e.right

    print(res)





    

if __name__ == "__main__":
    show_tree()
    inorder_loop(root)