class VotingException(Exception):
    def __init__(self,message):
        self.message = message
    def __str__(self):
        return f"{self.message}"

def voting(age):
    if age < 18:
        raise VotingException("You Cannot Vote")
    print("You can Vote")

try:
    age=int(input("Enter Age  "))
    voting(age)
except VotingException as ve:
    print(ve.message)