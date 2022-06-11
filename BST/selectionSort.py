from tkinter import PROJECTING


def getInd(arr,x):
    ind=0
    for i in range(len(arr)):
        if arr[i]<arr[ind]:
            ind=i
    return ind+x


def SelSort(arr):
    n=len(arr)
    for i in range(n-1):
        tempArr=arr[i:]
        minInd=getInd(tempArr,i)
        arr[minInd],arr[i]=arr[i],arr[minInd]
    return print(arr)


ar=[2,5,2,4,6,890,0,8,5,3,32]
print(ar)
SelSort(ar)
