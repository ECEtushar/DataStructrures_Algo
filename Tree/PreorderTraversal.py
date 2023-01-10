from Tree import root

def preorder(root):
    if root == None:
        return

    print(root.data,end=',')
    preorder(root.left)
    preorder(root.right)

def preorder_loop(root):
    if root == None:
        return None

    stack = [root]
    res = []
    while stack != []:
        curr = stack.pop()
        
        if curr.right != None:
            stack.append(curr.right)

        if curr.left!=None:
            stack.append(curr.left)

        res.append(curr.data) 
    
    return res

if __name__ == "__main__":
    print("Recursive -> ", end='')
    preorder(root)
    print('\n')

    print("Iterative -> ",preorder_loop(root))