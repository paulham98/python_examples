# myPackage 폴더
# C:/tmp/myPackage/__init__.py
# __init__.py
__all__=['A', 'B']
from com.week_2.come_2 import A, B

# myPackage/A 폴더
# C:/tmp/myPackage/A/__init__.py
# __init__.py
__all__=['testA']
from com.week_2.come_2 import testA

# C:/tmp/myPackage/A/testA.py
# testA.py
def sumn(n=0):
    s = 0
    for i in range(n+1):
        s += i
    return s

# myPackage/B 폴더
# C:/tmp/myPackage/B/__init__.py
__all__=['testB']
from com.week_2.come_2 import testB

# C:/tmp/myPackage/B/testB.py
# testB.py
def fact(n):
    if n <= 1:
        return n
    return n*fact(n-1)

import sys