
class BST:
    def __init__(self,root):
        self.root=root

    class Node:
        def __init__(self,key):
            self.k=key
            self.left=None
            self.right=None

    def insert(self,key):
        if self.root==None:
            self.root=self.Node(key)
            return self.root

        curr=self.root

        while curr!=None:
            parent=curr
            if key==curr.k:
                return self.root
            if key>curr.k:
                curr=curr.right
            elif key<curr.k:
                curr=curr.left

        if key>parent.k:
            parent.right=self.Node(key)
        else:
            parent.left=self.Node(key)
        

    def preorder(self,root):
        #root=getattr(self.root,root)
        if root!=None:
            print(root.k,end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    def floor(self,key):
        root=self.root
        if root==None:
            return print(None)
        if root.k==key:
            return print(key)

        import math
        curr=root
        closest= -math.inf
        while curr!=None:
            if curr.k==key:
                return print(key)
            if key>curr.k:
                closest=max(closest,curr.k)
                curr=curr.right
            elif key<curr.k:
                curr=curr.left
        if closest== -math.inf:
            return print(None)
        return print(closest)

    def ceil(self,key):
        root=self.root
        if root==None:
            return print(None)
        import math
        ceiling= math.inf
        curr=root
        while curr!=None:
            if curr.k==key:
                return print(key)
            if key>curr.k:
                curr=curr.right
            elif key<curr.k:
                ceiling=min(ceiling,curr.k)
                curr=curr.left
        if ceiling== math.inf:
            return print(None)
        return print(ceiling)


if __name__=='__main__':
    t1=BST(None)
    nodes=[10,5,15,12,30]

    for i in nodes:
        t1.insert(i)

    t1.preorder(t1.root)
    print('\n')
    t1.ceil(4)


    #        10
    #      /    \
    #     /      \
    #    5        15
    #   /  \     /  \
    #  NA  NA   12  30

            

