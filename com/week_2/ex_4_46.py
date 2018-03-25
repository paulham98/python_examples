import time
def checkTime(func):
    def wrapper(n):
        start = time.time()
        ret = func(n)
        end = time.time()
        print('Execution time : {0}'.format(end-start))
        return ret
    return wrapper

@checkTime
