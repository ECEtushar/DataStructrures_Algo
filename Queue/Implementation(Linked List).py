


class MyQueue:
    
    class Node:
        def __init__(self,data):
            self.data=data
            self.next=None

    def __init__(self):
        self.front=None
        self.rear=None
        self.sz=0

    def enqueue(self,x):
        node=self.Node(x)
        if self.front==None:
            self.front=self.rear=node
            self.sz+=1
        else: 
            self.rear.next=node
            self.sz+=1
            self.rear=node

    def dequeue(self):
        if self.sz==0:
            return None
        else:
            self.front=self.front.next
            self.sz-=1

    def getFront(self):
        if self.sz>0:
            return self.front.data
        else:
            return 'Queue is Empty!'

    def getRear(self):
        if self.sz>0:
            return self.rear.data
        else:
            return 'Queue is Empty!'





q=MyQueue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()

print(q.getFront(),q.getRear(),q.sz)
