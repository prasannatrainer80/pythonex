def demo():
    emp_dict = {
        "empno" : 1,
        "name" : "Prasanna",
        "gender" : "Male",
        "city" : "Hyderabad"
    }

    try:
        print("Employ No ", emp_dict["empno"])
        print("Employ Name ", emp_dict["name"])
        print("Gender  ", emp_dict["gender"])
        print("City  ", emp_dict["city"])
        print("Topic  ", emp_dict["topic"])
    except KeyError as ke:
        print("Key Passed not found ", ke)


demo()