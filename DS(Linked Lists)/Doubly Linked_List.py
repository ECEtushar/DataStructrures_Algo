class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None


'Function for insertion of Node at the begining'
def InsHead(head,x):
    node=Node(x)
    if head==None:
        return node
    node.next=head
    head.prev=node
    
    return node

'Function for insertion of Node at the end'
def InsTail(head,x):
    node=Node(x)
    if head==None:
        return node
    tail=head
    while tail.next!=None:
        tail=tail.next
    tail.next=node
    node.prev=tail
    return head

'Function for deleting head of a DLL'
def DelHead(head):
    if head==None or head.next==None:
        return None
    newHead=head.next
    newHead.prev=None
    head.next=None
    return newHead

'Function for deleting last node of a DL'
def DelTail(head):
    if head==None or head.next==None:
        return None
    else:
        tail=head
        while tail.next.next!=None:
            tail=tail.next
        tail.next=None
        return head
    
'Function for reversal for DLL using STACK'
def Rev(head):
    if head==None:
        return head
    elif head.next==None:
        return head
    else:
        stack=[]
        curr=head
        while curr!=None:
            stack.append(curr.data)
            curr=curr.next
            
        Stack_size=len(stack)-1
        curr=head
        while curr!=None:
            curr.data=stack[Stack_size]
            curr=curr.next
            Stack_size-=1
        return head
    
'Function for reversal for DLL using the fact that a DLL has next as well as previous nodes'
def Rev2(head):
    if head==None:
        return None
    elif head.next==None:
        return head
    else:
        curr=head
        prev=None
        while curr!=None:
            prev=curr
            curr.next,curr.prev=curr.prev,curr.next
            curr=curr.prev
        return prev

'<-----DRIVER CODE----->'
'Null<---10<----->20<------>30<-------->40------>Null'

head=None
head=InsTail(head,10)
head=InsTail(head,20)
head=InsTail(head,30)
head=InsTail(head,40)        

        

