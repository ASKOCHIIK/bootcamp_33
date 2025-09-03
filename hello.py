class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f'{self.name} is {self.age} years old.'

class Argen(Student):
    def __init__(self):
        super().__init__("Argen", 17)