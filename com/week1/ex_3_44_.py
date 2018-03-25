import sys
import traceback
try:
    raise Exception("Oops!")
except:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
    print(''.join('!!' + line for line in lines))
finally:
    print("pleasure")

