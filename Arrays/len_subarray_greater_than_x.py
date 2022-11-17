

def func(arr,x):
    res=[]
    count=0
    su=x
    for i in arr:
        if i==su:
            res.append(1)
        temp = su-i
        if temp == i:
            res.append(count+1)
            count = 0
            su=x
        if temp<0:
            count = 0
            su=x
        else:
            su=temp
            count+=1
        
        
        


    print(res)

arr=[1,4,45,6,0,49,3,52]
x=51
func(arr,x)
