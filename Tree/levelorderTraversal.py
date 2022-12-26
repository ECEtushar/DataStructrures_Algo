"""
In place of list we can also use deque data structure for optimised solution
"""
from Tree import show_tree, root


def levelOrder(root):
    arr = [root]

    while arr!=[]:
        curr = arr.pop(0)
        print(curr.data, end=' ')
        if curr.left!=None:
            arr.append(curr.left)
        if curr.right!=None:
            arr.append(curr.right)

        

show_tree()
levelOrder(root)

