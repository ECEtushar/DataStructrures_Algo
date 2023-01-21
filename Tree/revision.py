from Tree import root, show_tree
def all_order(root):
    if root == None:
        return None

    pre_o = []
    in_o  = []
    pos_o = []

    aux_stack = [[root, 1]]
    while aux_stack != []:
        top = aux_stack[-1]
        
        if top[1] == 1:
            pre_o.append(top[0].data)
            top[1]+=1
            if top[0].left:
                aux_stack.append([top[0].left,1])
        
        elif top[1] == 2:
            in_o.append(top[0].data)
            top[1]+=1
            if top[0].right:
                aux_stack.append([top[0].right,1])

        
        elif top[1] == 3:
            pos_o.append(top[0].data)
            aux_stack.pop()

    print("Preorder: ",pre_o,"\nInorder: ",in_o,"\nPostorder: ",pos_o)
    return

show_tree()
all_order(root)


