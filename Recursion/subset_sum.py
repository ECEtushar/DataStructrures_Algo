

def subsets(arr, s=0, res=[]):
    if arr==[]:
        res.append(s)
        return
    subsets(arr[1:], s=s, res=res)
    subsets(arr[1:], s=s+arr[0], res=res)


arr = [5,2,1]
r = []
subsets(arr, res=r)
print(r)    