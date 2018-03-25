try:
    z = 10 / 0
except ZeroDivisionError as e:
    print("ZeroDivisionError:",e.args)
except ArithmeticError as e:
    print("Arithmetic:",e.args)
finally:
    print('Goodbye')