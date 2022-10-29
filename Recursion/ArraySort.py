def sortArr(arr):
    if arr == []:
        return arr
    x=  arr.pop()
    sortArr(arr)
    placeSorted(arr,x)
    return arr

def placeSorted(arr,x):
    if arr==[] or arr[-1]<x:
        arr.append(x)
        return arr
    else:
        i = arr.pop()
        placeSorted(arr,x)
        arr.append(i)
        return arr

arr = [0,3,2,5,1,4,9]
sortArr(arr)
#arr.sort()
print(arr)