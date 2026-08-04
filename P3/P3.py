class C1:
    def set(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

class C2(C1):
    def mult(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

a=int(input("Enter First Number  "))
b=int(input("Enter Second Number  "))
c2=C2()
c2.set(a, b)
print(c2.sum())
print(c2.sub())
print(c2.mult())
print(c2.div())