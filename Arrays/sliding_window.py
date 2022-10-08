
def sliding_window(arr,k):
    if k>len(arr):
        return False

    s = sum(arr[:k])

    i=0
    j=k
    max_sum = s
    while j!=len(arr):
        temp = s + arr[k] - arr[i]

        if temp>max_sum:
            max_sum = temp
        j+=1
        i+=1

    return max_sum





if __name__ == "__main__":
    arr = [1,8,30,-5,20]
    k=4
    print(sliding_window(arr,k))