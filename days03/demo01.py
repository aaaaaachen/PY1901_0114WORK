

import os
import sys

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
        name=input("请输入您的姓名:")
        passwd=input("请输入您的密码：")
        print("注册成功")

    elif a==2:
        xing_ming=input("姓名：")
        mi_ma=input("密码：")

        if xing_ming=="wu":

            if mi_ma=="123":
                print("登陆成功")


                print("点击任意键继续....")
                #商品信息展示
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
                    print(sum)

                    pay=float(input("\t实付金额："))
                    print("\n")
                    input("点击任意键结算....")

                    if pay<sum:
                        print("error")

                    else:
                        print("~*~*~*~*~*~**~*~*~*~*~*~~*~*~*~*~**~~*")
                        print("\t商品名称：",arr[int(id)-1][1])
                        print("\t商品单价： ",arr[int(id)-1][2])
                        print("\t商品个数：",num)
                        print("\t应付金额：",sum)
                        print("\t实付金额：",pay)
                        print("\t找零：",pay-sum)
                        print("~*~*~*~*~*~**~*~*~*~*~*~~*~*~*~*~**~~*")





            else:
                print("密码错误")
                
        else:
            print("用户错误")
    
    elif a==3:
        print("退出")
        exit()
else:
    print("aaaa")
    # continue

                                       
