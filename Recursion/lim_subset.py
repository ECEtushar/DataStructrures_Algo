


def limSubset(arr,res,i=0,sz=0,temp=[]):
    if i==len(arr):
        if sz==3:
            res.append(temp)
        return
    limSubset(arr,res,i=i+1,sz=sz,temp=temp)
    limSubset(arr,res,i=i+1,sz=sz+1,temp=temp+[arr[i]])


res=[]
arr=[1,2,3,4]

limSubset(arr,res)
print(len(res))
for i in res:
    print(i)