def strEx():
    x=123
    print(type(x))
    y=str(x)
    print(type(y))
    name="Python Programming..."
    print(name[:])
    print(name[2:5])
    print(name[:-2])
    student="Sravanthi "
    print(student *3)
    msg = "  Hello EveryOne How are you   "
    print(msg)
    print(msg.strip())
    print(msg.upper())
    print(msg.lower())
    greeting="Welcome to Python Programming Trainer Prasanna"
    print(greeting.split())
    test="welcome#to#python#programming#Trainer#Prasanna"
    print(test.split("#"))
    list1=[12,52,23,77,11]
    print(max(list1))
    print(min(list1))
    print(max(greeting.split()))
strEx()