class First:
    def show(self):
        print("Show Method from Class First...")

class Second(First):
    def display(self):
        print("Display Method from Class Second...")

second=Second()
second.show()
second.display()