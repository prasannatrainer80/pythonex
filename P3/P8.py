class First:
    def show(self):
        print("Show Method from Class First...")

class Second(First):
    def show(self):
        super().show()
        print("Show Method from Class Second...")

second=Second()
second.show()