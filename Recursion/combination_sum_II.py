"""
Leetcode question 40
"""
def pprint(n):
    if n==0:
        return 
    pprint(n-1)
    print(n)
    


pprint(5)
