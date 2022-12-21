"""
This question is LeetCode 46.
NOTE: This solution is valid only when the array/string is distinct
"""

# Approach "I"
def permute(arr,res,n,i=0,temp=[],map=set()):
    if i==n:
        res.append(temp)
        return
    for x in range(n):
        if arr[x] not in map:
            map.add(arr[x])
            permute(arr,res,n,i=i+1,temp=temp+[arr[x]],map=map)
            map.remove(arr[x])
    

# Approach "II"
def permute2(arr,res,n,i=0):
    if i == n:
        x=arr.copy() # for creating a deep copy otherwise it will be a shallow copy and the output will be list of same list
        res.append(x)
        return

    for x in range(i,n):
        arr[i],arr[x] = arr[x],arr[i]
        permute2(arr,res,n,i=i+1)
        arr[x],arr[i] = arr[i],arr[x]
        
    


def main(arr, approach):
    all_permute = []
    n=len(arr)
    if approach == "I":
        permute(arr,all_permute,n)

    if approach == "II":
        permute2(arr,all_permute,n)
    
    if approach not in {"I","II"}:
        raise ValueError("There are only two approaches for this question i.e I, II")
    
    print(all_permute)
    return all_permute



if __name__ == "__main__":
    array=[1,2,3]
    main(array, "II")



