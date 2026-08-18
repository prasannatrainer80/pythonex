import json
student = {
    "Name": "Peter",
    "Roll_no": "0090014",
    "Grade": "A",
    "Age": 20,
    "Subject": ["Computer Graphics", 
    "Discrete Mathematics", "Data Structure"]
}

with open("c:/files/data.json", "w") as write_file:
    json.dump(student, write_file)