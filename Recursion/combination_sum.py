"""

"""
def combination_sum(arr,t,i=0,temp=[]):
    if i==len(arr):
        if t==0:
            print(temp)
        return
    e = arr[i]
    combination_sum(arr, t=t, i=i+1, temp=temp) #not considering e
    if t>=e:
        combination_sum(arr, t=t-e, i=i, temp=temp+[e]) #considering e


    
arr=[2,3,5]
t=8
x=[]
combination_sum(arr,t)