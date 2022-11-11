

def subsets(arr,s=0,res=[]):
    if arr==[]:
        res.append(s)
        return res
    e=arr[0]
    subsets(arr[1:],s=s,res=res)
    subsets(arr[1:],s=s+e, res=res)


arr=[5,2,1]
r=[]
subsets(arr,res=r)
print(r)    