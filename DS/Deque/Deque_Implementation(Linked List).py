#Implementation of Deque using Linked List


class MyDeque:

    '<-------Node class for creating nodes/items to be insert/remove------>'
    class Node:
        def __init__(self,data):
            self.data=data
            self.next=None
            self.prev=None

    '<----Constructor of MyDeque class---->'        
    def __init__(self):
        self.front=self.rear=None
        self.sz=0

    '<---- Inserts an item from the front side of the deque---->'
    def insertFront(self,x):
        node=self.Node(x)
        if self.sz==0:
            self.front=self.rear=node
        else:
            self.front.prev=node
            node.next=self.front

            self.front=node
        self.sz+=1

    '<---- Inserts an item from the rear side of the deque ---->'        
    def insertRear(self,x):
        node=self.Node(x)
        if self.sz==0:
            self.front=self.rear=node
        else:
            node.prev=self.rear
            self.rear.next=node
            self.rear=node
        self.sz+=1

    '<---- Deletes front item of the deque---->'
    def delFront(self):
        if self.sz==0:
            return 'Deque is empty!'
        elif self.sz==1:
            self.front=self.rear=None
            self.sz-=1
        else:
            self.front=self.front.next
            self.front.prev=None
            self.sz-=1

    '''
    <---For this method(delRear) in O(1) time we need doubly linked list otherwise,
    all the other method can be done only by using singly linked list---->
    '''
    '<---- Deletes rear item of the deque---->'
    def delRear(self):
        if self.sz==0:
            return 'Deque is empty!'
        elif self.sz==1:
            self.front=self.rear=None
            self.sz-=1
        else:
            self.rear=self.rear.prev
            self.rear.next=None
            self.sz-=1


    '<---- Returns front item of the deque---->'
    def getFront(self):
        if self.sz>0:
            return self.front.data
        return 'Deque is empty!'

    '<---- Returns rear item of the deque---->'
    def getRear(self):
        if self.sz>0:
            return self.rear.data
        return 'Deque is empty!'

    '<---- Returns True if the deque is empty, otherwise False---->'
    def isEmpty(self):
        if self.sz==0:
            return True
        else:
            return False


    '<----Returns the length of the deque---->'
    def size(self):
        return self.sz


'<----Driver Code---->'
d=MyDeque()
d.insertFront(10)
d.insertFront(20)
d.insertRear(30)
d.insertRear(40)
d.insertFront(1)
d.delFront()
d.delRear()
print(d.getFront(),' ',d.getRear(),' ',d.size())
d.delRear()
print(d.getFront(),' ',d.getRear(),' ',d.size())
d.delFront()
print(d.getFront(),' ',d.getRear(),' ',d.size())
d.delFront()
print(d.getFront(),' ',d.getRear(),' ',d.size())