from Tree import root, show_tree

def inorder(root):
    if root == None:
        return

    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)

def inorder_loop(root):
    if root is None:
        return
    
    stack = [root]
    res = []
    node = root.left
    while True:
        # if node is not null, put it in stack and move to its left node
        if node != None:
            stack.append(node)
            node = node.left
        
        # if node is null
        else:
            if stack == []:
                print(res)
                return
            # takeout top most element from stack
            curr_node = stack.pop()
            # print it
            res.append(curr_node.data)
            # make node = poped_element`s right
            node = curr_node.right

if __name__ == "__main__":
    show_tree()
    inorder_loop(root)