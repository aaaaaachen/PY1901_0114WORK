
import os
import sys
import random
import time

while True:
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
         continue
    elif a==2:
        print("系统正在升级中。。。。")
        name="wu"
        passwd="123"
        a=input("请输入姓名：")
        b=input("请输入密码：")
        if a==name and b==passwd:
            print("登陆成功")
            # time.sleep(3)
            os.system("cls")
            print("点击任意键继续....")

            #商城界面展示
            
            while True:
                os.system("cls")
                print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
                print("             1.购物商城")
                print("             2.休闲小游戏")
                print("             3.退出系统")
                print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
                print("      点击任意键继续：")
                print("\n\n\n\n")
                choice=input("请输入选项（按R键返回主菜单）：")
                if choice=="1":
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
                            continue
                elif choice=="2":
                    print("****************************************")
                    print("            1.石头剪刀布")
                    print("            2.老虎棒子鸡")
                    print("            3.猜数字")
                    print("****************************************")
                    choice=int(input("      请输入选项："))
                    if choice==1:
                        print("wait")
                    elif choice==2:
                        print("wait")
                    elif choice==3:
                        print("wait")
                    # else:
                    #     break
                elif choice=="3":
                    print("客官请慢走....")
                    sys.exit(1)
                elif choice=="R":
                    print("1s后退出...")
                    sys.exit(1)
                else:
                    continue
            


            # break
        else:
            print("用户或密码错误，请重新输入")
            continue
            
    elif a==3:
        print("系统正在升级中.....")
        break
    else:
        print("请重新输入")
        continue