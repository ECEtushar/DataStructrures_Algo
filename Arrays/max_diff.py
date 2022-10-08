"""
This is a standard question of Buy&Sell Stock-I
"""
def max_diff(arr):
    
    if arr == []:
        return "empty list passed"

    var_max = arr[1]-arr[0]
    var_curr = arr[0]
    for i in arr[1:]:
        temp = i-var_curr

        if temp>var_max:
            var_max = temp

        if temp<0:
            var_curr = i
    return var_max


if __name__ == "__main__":
    arr = [[2,3,10,6,4,8,1],[7,9,5,6,3,2],[10,20,30],[30,10,8,2]]
    for i in arr:
        res = max_diff(i)
        print(res)

    
