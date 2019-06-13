'''
面向对象
'''
class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def study(self):
        print("python学着真有意思")
    def eat(self):
        print("鱼香肉丝走一波？")
    def play(self):
        print(self.name,"晚自习cs嗯哼？")

class Phone:
    def __init__(self,brand,color,price):
        self.brand = brand
        self.color = color
        self.price = price

    def wechat(self):
        print("你媳妇来微信了。。。")


dashuaibi = Person("大帅比",20,"男")
dashuaibi.study()
dashuaibi.play()



