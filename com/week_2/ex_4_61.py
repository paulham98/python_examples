def coroutine(func):
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return(gen)
    return wrapper
@coroutine
def Accumulator(target, acc=0):
    while True:
        acc += yield
        target.send(acc)
#coroutine
def Printer():
           while True:
               value = (yield)
               print(value)
import time
import random
def randProducer(target):
    try:
        while True:
               try:
                   time.sleep(1)
                   value = random.randint(1, 10)
                   print("rand value=", value, end=' =>')
                   target.send(value)
               except Exception as e:
                   print("Exception", e)
    except KeyboardInterrupt:
        print("KeyboardInterrupt!")
    finally:
        print("===Done===")

randProducer(Accumulator(Printer()))
