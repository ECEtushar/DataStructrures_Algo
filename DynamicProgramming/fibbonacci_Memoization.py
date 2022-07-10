# Memoization is a way of optimising a recursive solution with storing previously solved sub-problem to prevent CPU usage
def fibb_memoization(i):
    if i == 1 or i == 0:
        return i
    memo = [0,1]
    for i in range(2,i+1):
        curr = memo[i-1]+memo[i-2]
        memo.append(curr)
    return memo[i]

if __name__ == '__main__':
    i = 9
res= fibb_memoization(i)
print(f'{i}th fibbonacci number is : {res}')
    