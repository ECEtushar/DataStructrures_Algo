# This solution is for optimising TOP-DOWN (memoization) solution  to BOTTOM-UP (tabulation)
# In this solution we will optimise the space


def climbStairs(n):
    if n in {0,1,2}:
        return n
    prev1 = 2 # this is the (n-1)th position
    prev2 = 1 # this is the (n-2)th position

    for i in range(3,n+1):
    
        temp = prev1 + prev2
        prev2 = prev1
        prev1 = temp
    
    return prev1


n=5
ans = climbStairs(n)
print(ans)