import timeit

if __name__=='__main__':
    l=range(100000)
    print(timeit.timeit('l.pop(-1)', setup='form __main__ import l', number=100000))
    print(timeit.timeit('l.pop(100000/2)', setup='form __main__ import l', number=100000))
    print(timeit.timeit('l.pop(-2)', setup='form __main__ import l', number=100000))
    
