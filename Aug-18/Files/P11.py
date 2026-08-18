import os

def create_file(filename):
    try:
        with open(filename,"w") as f:
            f.write("Hello World...\n")
        print("File  " +filename + " Created Successfully...")
    except IOError:
        print("Error: Coult not Create File  " +filename)

def read_file(filename):
    try:
        with open(filename,"r") as f:
            contents = f.read()
            print(contents)
    except IOError:
        print("Error: Could not Read File  " +filename)


def append_file(filename,text):
    try:
        with open(filename,"a") as f:
            f.write(text)
        print("Text Appended to the file " +filename)
    except IOError:
        print("Error: Could not Append to File  " + filename)

def rename_file(filename, new_filename):
    try:
        os.rename(filename, new_filename)
        print("The File " +filename + " Renamed as " +new_filename)
    except IOError:
        print("Error: Could not Rename file  " +filename)

def delete_file(filename):
    try:
        os.remove(filename)
        print("File with " +filename + " Deleted Successfully...")
    except IOError:
        print("Error:  Could not Delete File  " +filename)

filename="c:/files/ex.txt"
new_filename="c:/files/newex.txt"

create_file(filename)
read_file(filename)
append_file(filename,"This is Additional Text...")
read_file(filename)
rename_file(filename,new_filename)
read_file(new_filename)
delete_file(new_filename)