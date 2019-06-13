'''
宠物医院
'''
class Pet:
    def __init__(self,nickname,health):
        self.nickname = nickname
        self.health = health

    def recovey(self):
        self.health += 5
        print(self.nickname,"正在康复中......")

class PetHospital:
    def __init__(self,name):
        self.name = name

    def treat(self,pet):
        if isinstance(pet,Pet):
            while pet.health <= 60:
                pet.recovey()
                print(pet.nickname,"正在zhiliao中....")
            else:
                print("已经恢复健康》》》")
        else:
            print("宠物医院只接受宠物的治疗")

dog = Pet("二哈",30)

ph = PetHospital("renaiyiyuan")

ph.treat(dog)



