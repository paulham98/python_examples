try:
    z = 10/ 0
except:
    z = 0.1
finally:
    print("%f"%z)
    print("Goodbye")