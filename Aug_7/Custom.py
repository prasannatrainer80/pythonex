class NumberZeroException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"{self.message}"

class NegativeException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"{self.message}"

def sum(a, b):
    if a < 0 or b < 0:
        raise NegativeException("Negative Numbers Not Allowed...")
    elif a == 0 or b == 0:
        raise NumberZeroException("Zero is Invalid Value....")
    else:
        c = a + b
        print("Sum is  ", c)

try:
    a=int(input("Enter First Number  "))
    b=int(input("Enter Second Number  "))
    sum(a,b)
except NumberZeroException as e1:
    print(e1)
except NegativeException as e2:
    print(e2)
