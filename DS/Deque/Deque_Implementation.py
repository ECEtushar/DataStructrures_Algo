from collections import deque

'''       
deque class Methods---> [ 'append', 'appendleft', 'clear', 'copy', 'count', 
'extend', 'extendleft', 'index', 'insert', 'maxlen', 'pop', 'popleft', 'remove',
'reverse', 'rotate']            
 
 '''

#Below is an example of a type of Data Structure in which all the operations takes 'O(1)' time

class MyDS:
    def __init__(self):
        self.deq=deque()
        self.sz=0

    def insertMin(self,x):
        if self.sz==0:
            self.deq.append(x)
            self.sz+=1
        else:
            self.deq.appendleft(x)
            self.sz+=1

    def extractMin(self):
        if self.sz==0:
            return 'Deque is Empty'
        else:
            e=self.deq.popleft()
            self.sz-=1
            return e

    def insertMax(self,x):
        self.deq.append(x)
        self.sz+=1

    def extractMax(self):
        if self.sz==0:
            return 'Deque is Empty'
        else:
            e=self.deq.pop()
            self.sz-=1
            return e

    def getMin(self):
        if self.sz==0:
            return 'Deque is Empty'
        else:
            return self.deq[0]

    def getMax(self):
        if self.sz==0:
            return 'Deque is Empty'
        else:
            return self.deq[-1]
            
    def size(self):
        return self.sz


'<----Driver Code---->'
d=MyDS()
d.insertMin(10)
d.insertMin(5)
d.insertMax(20)
d.insertMin(3)
print(f'{d.extractMin()}\n{d.extractMax()}\n{d.getMin()}\n{d.getMax()}')
