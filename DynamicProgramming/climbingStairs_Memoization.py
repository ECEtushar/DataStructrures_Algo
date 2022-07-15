# This solution is for converting the recursive solution to DP solution (memoization)

# There are total two solution(top-dowm) for this problem


#--------Solution 1---------#

def climbStairs(n):
    x=[0 for i in range(n)]
    res = auxFunc(n,x)
    return res

def auxFunc(n,x):
    if n == 1 or n==2 or n==0:
        return n

    if x[n-1]==0:
        x[n-1] = auxFunc(n-1,x)
    if x[n-2] == 0:
        x[n-2] = auxFunc(n-2,x)

    return x[n-1]+x[n-2]



#--------Solution 2---------#

def climbStairs_iterative(n):
    if n in {0,1,2}:
        return n
    temp = [0,1,2]
    for i in range(3,n+1):
        temp.append(temp[i-1]+temp[i-2])

    return temp[n-1]+temp[n-2]


n=7
print(f'Answer from solution-1: {climbStairs(n)}')

print(f'Answer from solution-2 (iterative): {climbStairs_iterative(n)}')