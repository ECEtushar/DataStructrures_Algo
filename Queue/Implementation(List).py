class Queue:
    def __init__(self):
        self.que=[]
        self.sz=0
    def enqueue(self,data):
        if data==None:
            return self.que
        self.que.append(data)
        self.sz+=1
        return self.que
    def dequeue(self):
        if self.sz==0:
            return 'Queue is Empty'
        self.que.pop(0)
        self.sz-=1
        return self.que
    def size(self):
        return self.sz


'<------Driver Code------>'
q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.enqueue(40))
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.size())
print(q.dequeue())
print(q.dequeue())
print(q.size())