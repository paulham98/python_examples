try:
    z = 10/20
except ZeroDivisionError as e:
    print("ZeroDivisionError:",e.args)
except NameError as e:
    print("NameError:",e.args)
else:
    print("No exceptions")
finally:
    print("nice to meet you")