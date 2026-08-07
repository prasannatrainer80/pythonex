def show():
    try:
        names=["Pavan","Vignesh","Chandana",
               "James","Rahul"]
        print(names[10])
    except IndexError:
        print("Array Size is Small...")
    except:
        print("Some Error Occurred")
    else:
        print("No Exception in this Code...")
    finally:
        print("Program by Prasanna")

show()