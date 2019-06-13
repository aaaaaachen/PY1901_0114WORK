import random
num=random.randint(1,4)
num=int(num)
print("请输入您选择的动物：")
animal=int(input("1.老虎 2.棒子 3.鸡 4.虫子\n"))
if num==1:
    num1="老虎"
elif num==2:
    num1="棒子"
elif num==3:
    num1="鸡"
elif num==4:
    num1="虫子"

if animal>4:
    print("输入有误")
else:
    if (animal==1 and num==3)or\
       (animal==2 and num==1)or\
       (animal==3 and num==4)or\
       (animal==4 and num==2):

        print("系统输出：",num1)
        print("可把你牛逼坏了")
    elif(animal==1 and num==2)or\
        (animal==2 and num==4)or\
        (animal==3 and num==1)or\
        (animal==4 and num==3):

        print("系统输出：",num1)
        print("你可真菜。。")
    else:

        print("系统输出：",num1)
        print("en棋逢对手啊·不错不错")
 