
def buy_sell_stock(arr):
    profit = 0
    min_sf = arr[0]
    max_sf = arr[0]
    for i in arr:
        if i>max_sf:
            max_sf = i
        if i<max_sf:
            profit += max_sf - min_sf
            min_sf = i
            max_sf = i
    if max_sf>min_sf:
        profit += max_sf - min_sf
    return profit

if __name__  == "__main__":
    arr = [
            [1,5,3,8,12]
           ]
    for i in arr:
        res= buy_sell_stock(i)
        print(res)
    
            