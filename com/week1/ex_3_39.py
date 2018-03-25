try:
    z = 10 / 0
    print(z)
except (ZeroDivisionError, NameError) as e:
    print(e.args)
finally:
    print('Goodbye')

try:
    print(z)
    z = 10 / 0
except (ZeroDivisionError, NameError) as e:
    print(e.args)
finally:
    print('Goodbye')