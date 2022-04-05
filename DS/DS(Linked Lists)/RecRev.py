class Node:
    def __init__(self,k):
        self.k=k
        self.next=None

def insert(head,val):
    node=Node(val)
    if head==None:
        return node
    curr=head
    while curr.next!=None:
        curr=curr.next
    curr.next=node
    

def printL(head):
    curr=head
    while curr!=None:
        print(f'|{curr.k}|--->',end="")
        curr=curr.next
    print('null')

def Reverse(head):
    prev=None
    curr=head
    while curr!=None:
        nxt=curr.next
        curr.next=prev
        prev=curr
        curr=nxt
    return prev

def RecRev(head,prev=None):
    if head!=None:
        #return head
        head.next=RecRev(head.next,head)
        return prev
    
    


head=insert(None,10)
for i in range(20,50,10):
    insert(head,i)
printL(head)

RecRev(head)
printL(head)