class First:
    def show(self):
        print("Show Method from Class First...")

class Second(First):
    def display(self):
        print("Display Method from Class Second...")

class Third(Second):
    def company(self):
        print("Company is Wipro...")

third=Third()
first=First()
second=Second()
print(isinstance(third,Third))
print(isinstance(second,Second))
print(isinstance(first,First))