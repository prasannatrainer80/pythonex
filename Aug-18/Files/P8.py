def readFile():
    file=open("c:/files/PivotEx.py")
    for line in file:
        print(line)

try:
    readFile()
except FileNotFoundError:
    print("The File You are loking Does not Exist")