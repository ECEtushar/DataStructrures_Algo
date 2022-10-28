# Let say given an array arr = [3,2,4], the contigious subequence will be 
# [3,2,4], [3,2], [3,4], [2,4], [4]


def string_subsequence(arr,ind=0,temp=''):
    if ind >= len(arr):
        if temp!="":
            print(temp, end=", ")
        
        return
    e = arr[ind]
    string_subsequence(arr,ind=ind+1,temp=temp)
    string_subsequence(arr,ind=ind+1,temp=temp+e)
    

def array_subsequence(arr,ind=0,temp=[]):
    if ind>=len(arr):
        if temp!=[]:
            print(temp,end=", ")
        return
    e = arr[ind]
    array_subsequence(arr,ind = ind+1,temp=temp)
    array_subsequence(arr, ind=ind+1, temp= temp+[e])

if __name__ == "__main__":
    string_subsequence("ab")
    print("\n")
    array_subsequence([1,2,3])
    
    