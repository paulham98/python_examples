try:
    z = 10 / 0
except ZeroDivisionError as e:
    print("ZerodivisionError:", e.args)
finally:
    print("Hello")