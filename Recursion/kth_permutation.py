def permute(arr, res, n,i=0):
    if i==n:
        x=arr.copy()
        res.append(x)
        return

    for x in range(i,n):
        arr[i], arr[x] = arr[x], arr[i]
        permute(arr, res, n, i+1)
        arr[x], arr[i] = arr[i], arr[x]

def get_fact(n):
    if n==1:
        return 1
    return n*get_fact(n-1)

def main(n,k):
    arr= [i for i in range(1, n+1)]
    fact= get_fact(n-1)
    
    e = arr.pop((k-1)//fact) # to get the index of range that lies and valid for k
    res=[]
    permute(arr, res, n-1)
    res.sort()
    print([e]+res[(k-1)%fact]) # to get the index of the set in the range


main(3,1)