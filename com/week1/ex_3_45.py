try:
    x = -10
    assert x > 0, "need a positive number"
except AssertionError as e:
    print(e.args)
finally:
    print('Goodbye')