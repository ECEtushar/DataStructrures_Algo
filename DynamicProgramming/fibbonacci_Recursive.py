# ith Fibbonacci number is the sum of (ith - 1) + (ith - 2), hence reccurance relation of Fib(i) = Fib(i-1)+Fib(i-2)

def fibbonacci(i):
    if i == 1 or i == 0:
        return i
    return fibbonacci(i-1)+fibbonacci(i-2)


if __name__ == '__main__':
    i = 9
    res= fibbonacci(i)
    print(f'{i}th fibbonacci number is : {res}')
