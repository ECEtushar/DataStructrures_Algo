"""
Leetcode question 90
"""
def subsetII(arr,res,i=0,r=[]):
    res.append(r)
    for j in range(len(arr)):
        if r==[]:
            subsetII(arr,res,i=j+1,r=r+[arr[j]])
        else:
            if arr[j]!=r[-1]:
                subsetII(arr,res,i=j+1,r=r+[arr[j]])



res=[]
arr=[1,2,2]
subsetII(arr,res)
print(res)