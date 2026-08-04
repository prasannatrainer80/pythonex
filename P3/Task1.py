class Activity:
    def __init__(self, duration, description, numberOfParticipants):
        self.duration = duration
        self.description = description
        self.numberOfParticipants = numberOfParticipants

    def __str__(self):
        return "duration : " + str(
            self.duration) + ", description : " + self.description + ", numberOfParticipants : " + str(
            self.numberOfParticipants)


class Presentation(Activity):
    def __init__(self, duration, description, numberOfParticipants, title, numberOfSlides):
        super().__init__(duration,description,numberOfParticipants)
        self.duration = duration
        self.description = description
        self.numberOfParticipants = numberOfParticipants
        self.title = title
        self.numberOfSlides = numberOfSlides

    def __str__(self):
        return "duration : " + str(
            self.duration) + ", description : " + self.description + ", numberOfParticipants : " + str(
            str(self.numberOfParticipants) + ", title : " +self.title + ", numberOfSlides : " +str(self.numberOfSlides))


class CulturalEvent(Activity):
    def __init__(self, duration, description, numberOfParticipants, title, typeOfCulturalEvent):
       super().__init__(duration,description,numberOfParticipants)
       self.duration = duration
       self.description = description
       self.numberOfParticipants = numberOfParticipants
       self.title = title
       self.typeOfCulturalEvent = typeOfCulturalEvent

    def __str__(self):
        return "duration : " + str(
            self.duration) + ", description : " + self.description + ", numberOfParticipants : " + str(
            str(self.numberOfParticipants) + ", title : " + self.title + ", typeOfCulturalEvent : " + str(self.typeOfCulturalEvent))


obj1 = Presentation(int(input()), input(), int(input()), input(), int(input()))
obj2 = CulturalEvent(int(input()), input(), int(input()), input(), input())

print(obj1)
print(obj2)