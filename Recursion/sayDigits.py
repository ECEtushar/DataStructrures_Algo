def sayDigits(n,arr):
    if n==0:
        return 
    
    sayDigits(n//10,arr)
    print(arr[n%10],end=' ')


map=['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
sayDigits(67501,map)