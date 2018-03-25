try:
    raise Exception("Oops!")
except Exception as e:
    print("Exception:",e.args)
finally:
    print("Goodbye")