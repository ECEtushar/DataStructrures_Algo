def binarySearch(arr,x):

    right=len(arr)-1
    left=0
    
    while right>=left:
        #claculating mid of the array for left and right index
        mid = (left+right)//2
        
        #if mid is equal to the given element i.e if x is found
        if arr[mid]==x:
            return mid

        #if mid element is greater than x, neglect the right part and assigning right = mid-1
        elif arr[mid]>x:
            right=mid-1

        #if mid element is smaller than x, neglect the left part and assigning left = mid+1
        elif arr[mid]<x:
            left=mid+1

    #if x is not found in the whole array, return -1
    return -1

arr=[i for i in range(1,11)]
x=11

print(binarySearch(arr,x))