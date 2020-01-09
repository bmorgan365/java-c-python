
# try divide by zero
try:
    a = 5 / 0
except ZeroDivisionError:
    print("Exception caught, can't divide by zero")
else:
    print("No exception handled")

