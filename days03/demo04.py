import random
import os
os.system("cls")

print("PYTHON1901电商平台用户登录")
print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
print("        1.新用户注册")
print("        2.用户登录")
print("        3.退出系统")
print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
print("（温馨提示）请输入：")
a=int(input("请输入选项："))

if a==1:
    os.system("cls")
    name=input("请输入您的姓名:")
    passwd=input("请输入您的密码：")
    print("注册成功")

elif a==2:
    os.system("cls")
    xing_ming=input("姓名：")
    mi_ma=input("密码：")

    if xing_ming=="wu":

        if mi_ma=="123":
            print("登陆成功")


            print("点击任意键继续....")
            #商城界面展示
            os.system("cls")
            print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
            print("             1.购物商城")
            print("             2.休闲小游戏")
            print("             3.退出系统")
            print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
            print("      点击任意键继续：")
            print("\n\n\n\n")
            choice=input("请输入选项：")

            if choice=="1":
                 #商品信息展示
                os.system("cls")
                print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
                print("商品编号\t商品名称\t商品单价\t商品库存\t商品描述")
                print("1\t\t苹果\t\t5.00\t\t80\t\t又大又甜")
                print("2\t\t橘子\t\t4.00\t\t80\t\t不甜不要钱")
                print("3\t\t芒果\t\t8.00\t\t80\t\t味美多汁")
                print("4\t\t榴莲\t\t43.00\t\t80\t\t跟屎一样香")
                print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
                print("      点击任意键继续：")
                print("\n\n\n\n")
                arr=[[1,"苹果",5.00,80,"又大又甜"],\
                    [2,"橘子",4.00,80,"又大又甜"],\
                    [3,"芒果",8.00,80,"又大又甜"],\
                    [4,"榴莲",43.00,80,"又大又甜"]]
                    
                id=float(input("\t请选择需要购买的商品："))

                if id>len(arr):
                    print("\t無商品")

                else:
                    num=float(input("\t请选择购买商品的数量："))

                    sum=arr[int(id)-1][2]*num
                    print("\t您需要支付",sum,"元")

                    pay=float(input("\t实付金额："))
                    print("\n")
                    input("\t点击任意键结算....")

                    if pay<sum:
                        print("\terror")

                    else:
                        os.system("cls")
                        print("~*~*~*~*~*~**~*~*~*~*~*~~*~*~*~*~**~~*")
                        print("\t商品名称：",arr[int(id)-1][1])
                        print("\t商品单价：",arr[int(id)-1][2])
                        print("\t商品个数：",num)
                        print("\t应付金额：",sum)
                        print("\t实付金额：",pay)
                        print("\t找零:     ",pay-sum)
                        print("~*~*~*~*~*~**~*~*~*~*~*~~*~*~*~*~**~~*")

            elif choice=="2":
                os.system("cls")
                # 游戏类型显示
                print("****************************************")
                print("            1.石头剪刀布")
                print("            2.老虎棒子鸡")
                print("            3.猜数字")
                print("****************************************")
                
                choice=input("     请输入要玩游戏的选项..") 

                if choice=="1":
                                       
                    # #石头剪刀布
                    a=int(input("请输入 1：石头 2：剪刀 3：布\n"))
                    b=int(random.randint(1,3))

                    if a==1 and b==1:
                        print("用户：石头")
                        print("系统：石头")
                        print("\n")
                        print("平局")

                    elif a==1 and b==2:
                        print("用户：石头")
                        print("系统：剪刀")
                        print("\n")
                        print("恭喜您获胜！") 
                        
                    elif a==1 and b==3:
                        print("用户：石头")
                        print("系统：布")
                        print("\n")
                        print("不好意思，您输了") 
                        
                    elif a==2 and b==1:
                        print("用户：剪刀")
                        print("系统：石头")
                        print("\n")
                        print("不好意思，您输了") 
                        
                    elif a==2 and b==2:
                        print("用户：剪刀")
                        print("系统：剪刀")
                        print("\n")
                        print("平局")  
                        
                    elif a==2 and b==3:
                        print("用户：剪刀")
                        print("系统：布")
                        print("\n")
                        print("恭喜您获胜！")  
                        
                    elif a==3 and b==1:
                        print("用户：布")
                        print("系统：石头")
                        print("\n")
                        print("恭喜您获胜！") 
                        
                    elif a==3 and b==2:
                        print("用户：布")
                        print("系统：剪刀")
                        print("\n")
                        print("不好意思，您输了")  
                        
                    elif a==3 and b==3:
                        print("用户：布")
                        print("系统：布")
                        print("\n")
                        print("平局")   

                    else:
                        print("\n\n\n") 
                        print("您输入有误")

                elif choice=="2":
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

                elif choice=="3":
                    range1=int(input("请输入本局游戏的最小值："))
                    range2=int(input("请输入本局游戏的最大值："))
                    num=random.randint(range1,range2)
                    # guess=int(input("请输入你猜的数字："))
                    guess="guess"
                    n=0
                    while guess!=num:
                        n+=1
                        guess=int(input("请输入你猜的数字："))
                        if guess<num:
                            print("您猜的数小了...")
                            
                        else:       
                            print("您猜的数大了...")
                            
                    else:
                        print("恭喜您猜对了")
                        print("您一共猜了",n,"次哦！")

                else:
                    print("系统正在升级中.....")
            
            elif choice=="3":
                print("客观请慢走")

            else:
                print("没有此选项")

        else:
                print("您输入的账户或密码错误")
                            
    else:
        print("用户错误")
   
elif a==3:
    print("退出")
                                       
