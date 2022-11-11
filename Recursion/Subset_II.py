"""
Leetcode question 90
"""
def subsetII(arr,res,r=[]):
    if arr==[]:
        res.append(r)
        return

    subsetII(arr[1:],res,r=r)
    subsetII(arr[1:],res,r=r+[arr[0]])


res=[]
arr=[1,2,2]
subsetII(arr,res)
print(res)