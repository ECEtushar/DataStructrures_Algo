from Tree import root

def srch(root, n):
    if root == None:
        return False
    if root.k == n:
        return True
    if srch(root.left, n):
        return True
    elif srch(root.right, n):
        return True
    else:
        return False



'<- - - - Driver Code - - - ->'



for i in range(10, 500, 10):
    print(srch(root, i), f'n= {i}')
