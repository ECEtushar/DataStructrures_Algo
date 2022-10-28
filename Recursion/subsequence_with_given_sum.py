# Printing the subsequences with K sum usin recursion
def k_sum(arr,k,ind=0,temp=[],s=0):
    if ind>=len(arr):
        if s==k:
            print(temp)
        return
    
        
    e = arr[ind]
    k_sum(arr,k,ind=ind+1,temp=temp,s=s)
    k_sum(arr,k,ind=ind+1,temp=temp+[e],s=s+e)




if __name__ == "__main__":
    arr = [1,2,1]
    k_sum(arr,2)
