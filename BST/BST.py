class BST:
    def __init__(self,val):
        self.k=val
        self.left = None
        self.right = None

class Traversal:
    
    def inorder(self,root):
        if root!=None:
            self.inorder(root.left)
            print(root.k,end=' ')
            self.inorder(root.right)

    def postorder(self,root):
        if root!=None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.k,end=' ')

    def preorder(self,root):
        if root!=None:
            print(root.k,end=' ')
            self.preorder(root.left)
            self.preorder(root.right)
            
    def levelOrder(self,root):
        from collections import deque
        q=deque()
        q.append(root)

        while len(q)!=0:
            curr=q.popleft()
            print(curr.k,end=' ')
            if curr.left!=None:
                q.append(curr.left)
            if curr.right!=None:
                q.append(curr.right)
    

#         50
#       /    \
#      /      \
#     40       60
#    /  \     /  \
#   10  48   59   70

root = BST(50)
'<------LEFT SUB-TREE------->'
root.left = BST(40)
root.left.left = BST(10)
root.left.right = BST(48)

'<------RIGHT SUB-TREE------->'
root.right = BST(60)
root.right.left = BST(59)
root.right.right = BST(70)
if __name__=='__main__':
    tree=Traversal()
    tree.preorder(root)