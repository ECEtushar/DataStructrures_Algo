#------Implementation of Stack using List-------#

class Stack:
    def __init__(self):
        self.s=[]
        self.size=0
        
    '<----Push Operation---->'    
    def push(self,x):
        self.s.append(x)
        self.size+=1
        return self.s
    
    '<----pop operation---->'
    def pop(self):
        if self.size>0:
            self.s.pop(-1)
            self.size-=1
            return self.s
        return 'Stack is Empty!'

    '<----peek operation---->'
    def peek(self):
        if self.size>0:
            return self.s[-1]
        return 'Stack is Empty'
    
    '<----isEmpty Operation---->'
    def isEmpty(self):
        if self.size==0:
            return True
        return False

    '<----Size of Stack---->'
    def Size(self):
        return self.size



  
class MyStack:
    
    class Node:
        def __init__(self,data):
            self.data=data
            self.next=None  
    
    def __init__(self):
        self.head=None
        self.s=0

    def push(self,x):
        node = self.Node(x)
        if self.head==None:
            self.head=node
            self.s+=1
            return self.head.data
        else:
            node.next=self.head
            self.s+=1
            self.head=node
            return self.head.data

    def pop(self):
        if self.s!=0:
            poped=self.head.data
            temp=self.head.next
            self.head=temp
            self.s-=1
            return poped
        return 'Stack is Empty'
    
    def peek(self):
        if self.s==0:
            return 'Stack is Empty!'
        return self.head.data
    
    def isEmpty(self):
        if self.s==0:
            return True
        else:
            return False

    def size(self):
        return self.s
    

s=MyStack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)

def pri(s):

    curr=s.head
    while curr!=None:
        print(curr.data)
        curr=curr.next