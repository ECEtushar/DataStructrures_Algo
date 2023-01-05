from Tree import root, show_tree

def postorder(root):
    if root == None:
        return
    
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=',')
    
def postorder_loop(root):
    if root is None:
        return None
    
    stack = [root]
    res=[]

    while stack != []:
        # take out topmost element from stack
        curr = stack.pop()

        # check wether left of curr is null
        if curr.left != None:
            stack.append(curr.left)
        
        # check wether right of curr is null
        if curr.right!=None:
            stack.append(curr.right)
            
        #put the poped element to 2nd stack (res)
        res.append(curr.data)



    return res[::-1]

if __name__ == "__main__":
    show_tree()
    postorder(root)
    print("\n")
    print("Iterative -> ",postorder_loop(root))