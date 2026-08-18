with open("c:/files/PivotEx2.py","r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)

        