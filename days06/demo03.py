# xiyouji = ("猪八戒","沙僧","唐僧",["孙悟空","齐天大圣"],"猪八戒")
#
# print(xiyouji)
# a = xiyouji.count("猪八戒")
# b = xiyouji.index("唐僧")
# xiyouji[3][1] = "土行孙"
# xiyouji[3][0] = "死猴子"
#
# print(a)
# print(b)
# print(xiyouji)
#
# name = {"tom","jerry","rose","robet"}
# print(name)
# name.add("james")
# print(name)
# name1 = name.copy()
# print(name1)
# name1.remove("rose")
# print(name1)
# name1.add("lucy")
# print((name1))
# name2 = name&name1
# print(name2)
# name3 = name|name1
# print(name3)
# a = name1.__eq__(name)
# print(a)
# name3.pop()
# print(name3)
# name3.pop()
# name3.pop()
# name3.pop()
# name3.pop()
# print(name3)
# c = name3.symmetric_difference(name)
# print(c)
# # 更新具有自身和另一个对称差的集合
# print(name)
# print(name3)
# name3.symmetric_difference_update(name)
# print(name3)
# waaa = set([1,2,3])
# haaa = set([1,3,5])
# print(waaa)
# print(haaa)
# # 使用自身和其他集合的并集更新集合
# haaa.update(waaa)
# print(haaa)

# d = {1 : 2,2 : "shabi"}
# print(d)
# dict = {"name":"jerry","age":17,"sex":"female"}
# print(dict)
# print("dict:['age']",dict['age'])
# dict["age"] = 18
# print(dict)
# tuple.index()
while True:
    a = True
    for i in range(1,10):
        if i == 3:
            print("展廳")
            a = False

        print("zhiwei",i)
    if a:
        break
    else:
        print("ting")


