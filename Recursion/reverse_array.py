def insert_beg(arr,x):
    if arr==[]:
        arr.append(x)
        return
    
    y = arr.pop()
    insert_beg(arr,x)
    arr.append(y)



def rev_arr(arr):
    if len(arr) == 1:
        return arr

    x= arr.pop()
    rev_arr(arr)
    insert_beg(arr,x)
    return arr
    

if __name__ == "__main__":

    a=[1,2,3,4,45]
    print(rev_arr(a))
    