#This question is very deep conceptual and its advised to rewise it time to time

def kthgrammar(n,k):
    if n==1 and k==1:
        return 0
    total = 2**(n-1)
    
    mid = total//2
    if k<=mid:
        return kthgrammar(n-1,k)
    else:
        return int(not kthgrammar(n-1,k-mid))

n = 3
k = 3

l=kthgrammar(n,k)
print(l)