src=open("c:/files/PivotEx2.py","r")
tar=open("c:/files/out.txt","w")
for line in src:
    # print(line)
    tar.write(line)

print("File Copied...")