'''
老张开车去东北
'''

class Person:
    def __init__(self,name,card):
        self.name = name
        self.card = card

    def drive(self,car,place):
        # print(self.name,"开",car.brand,"去",place.name)
        if self.card:
            print("{}开着{}的{}去{}钓鱼".format(self.name,car.color,car.brand,place.name))
        else:
            print("北京第三安全局提醒您：道路千万条，安全第一条，行车不规范，亲人两行泪")

class Car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color

class Place:
    def __init__(self,name):
        self.name = name

lao_zhang = Person("老张",False)
lao_liu = Person("老刘",True)
car = Car("jeep","灰色")
place = Place("东北")

lao_zhang.drive(car,place)
lao_liu.drive(car,place)

