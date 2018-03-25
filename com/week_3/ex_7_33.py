# C:/tmp/testFact.py
def fact(n):
    if n <= 1:
        return n
    return n*fact(n-1)

n = int(input('input n:'))
n2 = fact(n)
print(n2)

import os
os.chdir('C:/tmp')
os.system('pyinstaller -F testFact.py')
input n:5


