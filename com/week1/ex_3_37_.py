try:
    z = 10 /0
except ArithmeticError as e:
    print("ArithmeticError:",e.args)
except ZeroDivisionError as e:
    print("Zerodivisionerror:",e.args)
finally:
    print('Goodbye')