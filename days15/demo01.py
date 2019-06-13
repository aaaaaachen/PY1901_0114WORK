class Person:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"{self.name}吃冰激凌")

class Student:
    super()

p = Person("大帅比")
p.eat()