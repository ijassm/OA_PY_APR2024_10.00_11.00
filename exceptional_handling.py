# Exceptional handling
sakthi = "Good Boy"

try:
    print("First Try")
    print(5 / 2)
    print(sakthi)
    print(5 + "5")

except ZeroDivisionError:
    print("Can't divide by zero")

except NameError:
    print("Please check your varibale is decalared or not")

except Exception as error:
    print("Something went wrong : ", error)

else:
    print("No exception occurred")

finally:
    print("Finally block executed")
