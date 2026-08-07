def division():
    try:
        a = int(input("Enter First Number   "))
        b = int(input("Enter Second Number  "))
        c = a / b
        print("Division ", c)
    except ValueError:
        print("String Cannot be Converted as Number")
    except ZeroDivisionError:
        print("Division By Zero Impossible...")
    finally:
        print("Code from ECE 3rd Year")

division()