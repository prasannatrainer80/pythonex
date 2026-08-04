class First:
    def show(self):
        print("Show From Class First...")

class Second:
    def display(self):
        print("Display Method from Class Second...")

class Third:
    def test(self):
        print("Test Method from Class Third...")

class Final(First,Second,Third):
    def demo(self):
        print("Demo Method from Final Class")

final=Final()
final.show()
final.display()
final.test()
final.demo()
print(issubclass(Final,First))
print(issubclass(Final,Second))
print(issubclass(Final,Third))