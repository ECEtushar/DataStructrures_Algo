from sample_tree import root

class Traversal:
    def __init__(self,root):
        self.root=root

    '<------PreOrder Traversal------->'
    def preOrd(self,root,ls):
        if root==None:
            return []
        ls.append(root.k)
        self.preOrd(root.left,ls)
        self.preOrd(root.right,ls)

    def Preorder(self):
        ls=[]
        self.preOrd(self.root,ls)
        return print('Preorder: ',ls)

    '<------PostOrder Traversal------->'
    def posOrd(self,root,ls):
        if root==None:
            return []

        self.posOrd(root.left,ls)
        self.posOrd(root.right,ls)
        ls.append(root.k)

    def Postorder(self):
        ls=[]
        self.posOrd(self.root,ls)
        return print('Postorder: ',ls)

    '<------InOrder Traversal------->'

    def inOrd(self, root, ls):
        if root == None:
            return []
        self.inOrd(root.left, ls)
        ls.append(root.k)
        self.inOrd(root.right, ls)


    def Inorder(self):
        ls = []
        self.inOrd(self.root, ls)
        return print('Inorder: ', ls)

if __name__=='__main__':
    trav = Traversal(root)
    trav.Preorder()
    trav.Postorder()
    trav.Inorder()