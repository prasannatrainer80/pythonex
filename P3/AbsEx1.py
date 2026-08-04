from abc import abstractmethod


class Training:
    @abstractmethod
    def name(self):
        pass
    @abstractmethod
    def email(self):
        pass

class Debashis(Training):
    def name(self):
        print("Hi I am Debashis")

    def email(self):
        print("email is debashis@gmail.com")

class Sindhu(Training):
    def name(self):
        print("Hi I am Sindhu...")

    def email(self):
        print("Email is sindhu@gmail.com")

class Bala(Training):
    def name(self):
        print("Name is Bala")

    def email(self):
        print("Email is bala@gmail.com")

training1=Debashis()
training2=Sindhu()
training3=Bala()

training1.name()
training1.email()
training2.name()
training2.email()
training3.name()
training3.email()

list=[training1,training2,training3]
for training in list:
    training.name()
    training.email()