'''
面向对象案例：
	老张开车去东北
	案例分析：
	对象有：人
		   交通工具
		   地点
'''
#定义人的对象
class Person:
#初始化人的属性
    def __init__(self,name,card):
        self.name = name
        self.card = card

	#定义人使用交通工具的方法

    def drive(self,tool,place):
        if self.card:
            tool.driving()
            print("{}开{}去{}".format(self.name,tool.name,place.name))
        else:
            print("北京第三安全局提醒您：道路千万条，安全第一条，行车不规范，亲人两行泪")


#定义交通工具的对象
class Traffic_Tools:
	#初始化交通工具的属性
	def __init__(self,name,color):
		self.name = name
		self.color = color
	#定义交通工具的启动方法
	def driving(self):
		print("{}已经启动".format(self.name))

#定义地点的对象
class Place:
	#初始化地点的属性
	def __init__(self,name):
		self.name = name

lao_zhang = Person("老张",False)
tool = Traffic_Tools("Jeep","灰色")
place = Place("东北")

lao_zhang.drive(tool,place)