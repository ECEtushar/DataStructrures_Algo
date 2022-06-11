
def recursiveBinarySearch(arr,left,right,x):

    #Base Case i.e if left is greater than right which means x is not found
    if left>right:
        return -1

    # Calculating the mid of given left and right
    mid = (left+right)//2

    # if arr[mid] is equal to x, i.e x is found
    if arr[mid]==x:
        return mid

    # if arr[mid] > x
    elif arr[mid]>x:
        right = mid - 1
        return recursiveBinarySearch(arr,left,right,x)

    # if arr[mid] < x
    else:
        left = mid + 1
        return recursiveBinarySearch(arr,left,right,x)

if __name__ == '__main__':
    arr = [2,10,13,24,54,68,100]
    x = 101
    left = 0
    right = len(arr)-1
    print(recursiveBinarySearch(arr,left,right,x))
