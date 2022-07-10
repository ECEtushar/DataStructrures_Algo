# Tabulation is space optimisation over memoization

def fib_tabulation(i):
    if i == 1 or i == 0:
        return i
    prev = 1
    prev2 = 0
    
    for i in range(2,i+1):
        curr = prev + prev2
        prev2 = prev
        prev= curr
    return prev

if __name__ == '__main__':
    i = 0
    res= fib_tabulation(i)
    print(f'{i}th fibbonacci number is : {res}')