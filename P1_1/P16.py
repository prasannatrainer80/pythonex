course = input("Enter Course Name  ")
match course:
    case "Java":
        print("Java Training")
    case "Python":
        print("Python Training")
    case "Php":
        print("Php Training")
    case "React":
        print("React Training...")
    case "Angular":
        print("Angular Training...")
    case _:
        print("Invalid Option")
