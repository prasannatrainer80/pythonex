class Demo:
    __privateStr="Prasanna"
    _protectedStr="Wipro"
    publicStr="Great Learning"

class Test(Demo):
    def show(self):
        print(self.publicStr)
        print(self._protectedStr)

test=Test()
print(test.publicStr)
print(test._protectedStr)
# print(test.__privateStr)