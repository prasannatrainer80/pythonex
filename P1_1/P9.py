sname = input("Enter Student Name  ")
course = input("Enter Course Name  ")
company = input("Enter Company Name  ")
formatStr= "{{ Student Name {}, Student Course {}, Student Company {} }}."
result = formatStr.format(sname, course, company)
print(result)