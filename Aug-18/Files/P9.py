def read_file():
    try:
        with open("c:/files/tesme.txt","r") as f:
            contents=f.read()
            print(contents)
    except FileNotFoundError:
        print("The File You are Looking Does not Exist...")

read_file()