"""
This is a approach in which we can get the preorder, postorder and inorder in single iteration of tree
"""
from Tree import root, show_tree


def all_orders(root):
    if root is None:
        return 
    # defining all the order stacks
    preorder = []
    postorder = []
    inorder = []
    
    #initial config of base stack
    stack = [[root,1]] # base stack will have element in order [[node, num], [node, num], ....]

    while stack!=[]:
        # taking the top most element of base stack
        peek = stack[-1]

        # if num of top most element is 1, means it will go in preorder
        if peek[1] == 1:
            # adding to preorder list
            preorder.append(peek[0].data)
            # incrementing its num by 1, so that it can become 2
            peek[1]+=1
            # if its left exists, put it in the base stack
            if peek[0].left:
                stack.append([peek[0].left,1])

        # if num of top most element is 2, means it will go in inorder
        elif peek[1] == 2:
            # adding to inorder list
            inorder.append(peek[0].data)
             # incrementing its num by 1, so that it can become 3
            peek[1]+=1
            # if its right exists, put it in the base stack
            if peek[0].right:
                stack.append([peek[0].right,1])

        # if num of top most element is 3, means it will go in postorder
        elif peek[1] == 3:
            # adding to postorder list
            postorder.append(peek[0].data)
            # finally after reaching to 3, its time to pop it from the base stack
            stack.pop()
    res= {}
    res["preorder"] = preorder
    res["inorder"] = inorder
    res["postorder"] = postorder
    return res

if __name__ == "__main__":
    ans = all_orders(root)
    show_tree()
    print(ans)