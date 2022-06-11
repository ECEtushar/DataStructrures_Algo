class MyQueue:

    class Node:
        def __init__(self,data):
            self.data=data
            self.next=None
    
    def __init__(self,cap):
        self.cap=cap
        self.front=None
        self.rear=None
        self.sz=0

    def enqueue(self,k):
        node=self.Node(k)
