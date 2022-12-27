from Tree import root

def preorder(root):
    if root == None:
        return

    print(root.data,end=',')
    preorder(root.left)
    preorder(root.right)

def preorder_loop(root):
    if root is None:
        return None
    st = [root]
    res=[]
    while st!=[]:
        curr = st.pop()
        res.append(curr.data)
        if curr.right != None:
            st.append(curr.right)
        if curr.left != None:
            st.append(curr.left)
    return res

if __name__ == "__main__":
    print("Recursive -> ", end='')
    preorder(root)
    print('\n')

    print("Iterative -> ",preorder_loop(root))