dayName=input("Enter DayName (First 3 Chars) ")
match dayName:
    case "Mon":
        print("Its Monday...")
    case "Tue":
        print("Its Tuesday...")
    case "Wed":
        print("Its Wednesday...")
    case "Thu":
        print("Its Thursday...")
    case "Fri":
        print("Its Friday...")
    case "Sat":
        print("Its Saturday...")
    case "Sun":
        print("Its Sunday...")
    case _ :
        print("Invalid Day")
