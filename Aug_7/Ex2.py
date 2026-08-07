def show():
    try:
        names=["Pavan","Vignesh","Chandana",
               "James","Rahul"]
        print(names[10])
    except IndexError:
        print("Array Size is Small...")

show()