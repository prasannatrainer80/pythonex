class Student:
    college = "Jbit"
    @classmethod
    def show_college(cls):
        print("College:", cls.college)

Student.show_college()