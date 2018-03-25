import time
def checkTime(func):
    bRunning = False
    def wrapper(*args, **kwargs):
        nonlocal bRunning
        if bRunning:
               return func(*args, **kwargs)
        # else
        bRunning = True
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        bRunning = False
        print("Execution time : {0}".format(end-start))
        return ret
    return wrapper
