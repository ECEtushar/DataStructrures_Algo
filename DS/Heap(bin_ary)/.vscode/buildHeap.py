def heapify(heap,i=0):
    l=(2*i)+1
    r=(2*i)+2
    if r<len(heap) and l<len(heap):
        minE=min(heap[l],heap[r],heap[i])
        if minE==heap[i]:
            return heap
        elif minE==heap[l]:
            heap[l],heap[i]=heap[i],heap[l]
            heapify(heap,l)
        elif minE==heap[r]:
            heap[r],heap[i]=heap[i],heap[r]
            heapify(heap,r)
    return heap


def buildHeap(arr):
    if arr==[]:
        return None
    node1=(len(arr)-2)//2
    while node1!=-1:
        heapify(arr,node1)
        node1-=1
    return print(arr)

if __name__=='__main__':
    arr=[10,5,2,20,1,40,15,5,11]
    buildHeap(arr)