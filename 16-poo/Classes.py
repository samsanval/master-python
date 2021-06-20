class Person:

    def getname(self):
        return self.name

    def getsurname(self):
        return self.surname

    def getheight(self):
        return self.height

    def getage(self):
        return self.age

    def setname(self, name):
        self.name = name

    def setsurname(self, surname):
        self.surname = surname

    def setage(self, age):
        self.age = age

    def setheight(self, height):
        self.height = height

    def walking(self):
        return "I'm walking"

    def sleep(self):
        return "I'm sleeping"


class Developer(Person):

    def __init__(self):
        self.languages = "HTML, CSS, Javascript, PHP, Python"
        self.experience = 5

    def getlanguages(self):
        return self.languages

    def learn(self, language):
        self.languages += language
        return self.languages

    def program(self):
        return "I'm programming"


class Technician(Developer):

    def __init__(self):
        super().__init__()
        self.audition = 'Expert'

    def audit(self):
        return self.audition