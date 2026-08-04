from abc import abstractmethod

class Animal:
    @abstractmethod
    def name(self):
        pass
    @abstractmethod
    def type(self):
        pass

class Lion(Animal):
    def name(self):
        print("Name is Lion...")

    def type(self):
        print("Its Wild Animal...")

class Cow(Animal):
    def name(self):
        print("Name is Cow...")

    def type(self):
        print("Its Mammals Category...")

class Crocodile(Animal):
    def name(self):
        print("Name is Crocodile...")

    def type(self):
        print("Its Water Animal...")

lion=Lion()
cow=Cow()
crocodile=Crocodile()

animals=[lion,cow,crocodile]
for animal in animals:
    animal.name()
    animal.type()