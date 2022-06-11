# basic heap class implementation having methods =[getRight, getLeft, getParent, Insert]

class Heap:
    def __init__(self):
        self.heap=[]
        self.sz=0

    def getParent(self,i):
        return (i-1)//2
        
    def getLeft(self,i):
        return (i*2)+1

    def getRight(self,i):
        return (i*2)+2

    def Insert(self,key):
        self.heap.append(key)
        self.sz+=1

        if self.heap==[]:
            return print(self.heap)
        
        n=len(self.heap)-1
        while n>0:
            parInd=self.getParent(n)
            if self.heap[parInd]>self.heap[n]:
                self.heap[n],self.heap[parInd]=self.heap[parInd],self.heap[n]        
            n=parInd
        return print(self.heap)


if __name__=='__main__':
    h=Heap()
    keys=[2,3,5,21,6,4,54,76,34,78,4]
    for key in keys:
        h.Insert(key)

    print(h.sz)

        