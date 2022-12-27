from Tree import root, show_tree

def inorder(root):
    if root == None:
        return

    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)

def inorder_loop(root):
    if root ==None:
        return
    stk =[root]
    res=[]
    while stk!=[]:
        if stk[-1].left!=None:
            stk.append(stk[-1].left)
        else:
            curr = stk.pop()
            res.append(curr.data)
            if curr.right != None:
                stk.append(curr.right)
            else:
                curr = stk.pop()
                res.append(curr.data)
    print(res)





    

if __name__ == "__main__":
    show_tree()
    inorder_loop(root)