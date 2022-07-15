# Find all the possible ways to climb a stairs if only one or two steps are allowed

def climbStairs(n):
    if n in {0,1,2}:
        return n
    
    s1 = climbStairs(n-1)
    s2 = climbStairs(n-2)
    return s1+s2

n = 5
f = climbStairs(n)
print(f'There are {f} ways to jump down from stairs')