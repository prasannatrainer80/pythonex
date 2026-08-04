class Employ:
    __empno=1
    __name="Prasanna"
    __basic=83234

    def show(self):
        print("Employ No ",self.__empno)
        print("Employ Name  ",self.__name)
        print("Basic ",self.__basic)

emp = Employ()
emp.show()