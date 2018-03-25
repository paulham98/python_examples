try:
    raise Exception("Oops!")
except Exception as e:
    print("Exception:",e.args)
    raise
finally:
    print('Goodbye')