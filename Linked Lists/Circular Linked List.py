class node:
    def __init__(self,k):
        self.k=k
        self.next=None

def Print(head):
    
    temp=head
    count=0
    while temp.next!=head:
        print(temp.k,end='-->')
        temp=temp.next
        count+=4
    s=count*'-'
    sp=count*' '
    print(temp.k,end='-')
    print(f'''{sp}
|{sp}|
 {s}''')

def DelH(head):
    if head==None:
        return None
    elif head.next==head:
        return None
    else:
        tail=head
        while tail.next!=head:
            tail=tail.next
        tail.next=head.next
        return head.next

def DelK(head,k):
    if k==1:
        DelH
    else:
        temp=head
        for i in range(1,k-1):
            temp=temp.next
        temp.next=temp.next.next
        return
        

head=node('A')
head.next=node('B')
head.next.next=node('C')
head.next.next.next=node('D')
head.next.next.next.next=node('E')
head.next.next.next.next.next=head

    
