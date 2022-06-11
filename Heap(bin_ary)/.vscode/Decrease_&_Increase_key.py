from heapify import heapify

#while decrease a key at any given index we need to travese the heap from BOTTOM to TOP so we need to use parent swap
def decrease(heap,i,key):
    if i>=len(heap):
        raise Exception("Index out of range!")

    heap[i]=key
    curr=i
    while curr>0:
        par=(curr-1)//2
        if heap[par]>heap[curr]:
            heap[par],heap[curr]=heap[curr],heap[par]
        curr=par
    return print(heap)



#while increase a key at any given index we need to travese the heap from TOP to BOTTOM so we need to use heapify
def increase(heap,i,key):
    if i>=len(heap):
        raise Exception("Index out of range!")
    heap[i]=key
    newHeap=heapify(heap,i)
    return print(newHeap)


if __name__=='__main__':
    heap=[2, 3, 4, 21, 4, 5, 54, 76, 34, 78, 6]
    #decrease(heap,9,1)
    increase(heap,1,110)
