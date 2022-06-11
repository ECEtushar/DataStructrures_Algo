def extractMin(heap):
    if heap==[] or heap==None:
        import math
        return -math.inf
    heap[0],heap[-1]=heap[-1],heap[0]
    minHeap=heap.pop()
    ResHeap=heapify(heap)
    fstring=f'heap: {ResHeap}\nMin: {minHeap}'
    return print(fstring)


def heapify(heap,i=0):
    lc=(i*2)+1
    rc=(i*2)+2
    if lc<len(heap) and rc<len(heap):
        minH=min(heap[lc],heap[rc],heap[i])
        if minH==heap[i]:
            return heap
        elif minH==heap[lc]:
            heap[lc],heap[i]=heap[i],heap[lc]
            heapify(heap,lc)
        elif minH==heap[rc]:
            heap[i],heap[rc]=heap[rc],heap[i]
            heapify(heap,rc)
    return heap

if __name__=='__main__':
    heap=[2, 3, 4, 21, 4, 5, 54, 76, 34, 78, 6]
    extractMin(heap)

            
