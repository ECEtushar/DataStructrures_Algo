
def subarr_sum(arr,sums):
    si = 0
    ei = 1
    curr=arr[0]
    while ei!=len(arr):
        if curr>sums:
            curr -= arr[si]
            si+=1
        if curr<sums:
            curr+=arr[ei]
            ei+=1

        if curr == sums:
            return [si,ei-1]

    return False
        



if __name__ == "__main__":
    arr = [1,4,20,3,10,5]
    s=20
    print(subarr_sum(arr,s))