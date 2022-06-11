from heapify import heapify


def delKey(heap,i):
    if i>len(heap):
        raise Exception('Index out of range!')
    heap[i]=heap[-1]
    heap.pop()
    heapify(heap,i)
    return print(heap)

heap=[2, 3, 21, 5, 54, 76, 34, 78, 6]
delKey(heap,2)