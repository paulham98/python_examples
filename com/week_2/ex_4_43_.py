import sys
try:
    raise Exception("Oops!")
except Exception as e:
    print("Exception:",e.args)
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print("exc_type", exc_type)
    print("exc_value", exc_value)
    print("exc_traceback", exc_traceback)
finally:
    print('Goodbye')