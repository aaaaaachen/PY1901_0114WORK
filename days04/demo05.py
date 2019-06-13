
import os
import sys
import random
import time


users=[["wu","123"]]
while True:
    os.system("cls")
    print("PYTHON1901电商平台用户登录")
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
    print("        1.新用户注册")
    print("        2.用户登录")
    print("        3.退出系统")
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
    print("（温馨提示）请输入：")
    a=int(input("   请输入选项："))
    #用户注册 
    if a==1:
         os.system("cls")
         username=input("请输入您的姓名:")
         passwd=input("请输入您的密码：")
         c_passwd=input("请再次输入您的密码:")
         
         if username=="" or passwd=="" or c_passwd=="":
             print("用户名或密码不能为空")
         elif passwd != c_passwd:
             print("两次输入密码不一致")
         else:
             print("注册成功")
             users.append([username,passwd])
         time.sleep(1)
         continue

         
    elif a==2:
        username=input("    请输入您的姓名")
        passwd=input("    请输入您的密码")
        
        for user in users:

            if user[0]==username and user[1]==passwd :
                print("登陆成功")
                time.sleep(3)
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

                        while True:
                            os.system("cls")
                            #商品展示
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

                                residue=arr[int(id)-1][3]-num

                                # 商品库存
                                # print("sssss",residue)

                                sum=arr[int(id)-1][2]*num
                                print("\t您需要支付",sum,"元")

                                pay=float(input("\t实付金额："))
                                print("\n")
                                input("\t点击任意键结算....")

                                if pay<sum:
                                    print("\terror")
                                    print("请您付全款，谢谢")
                                    time.sleep(2)
                                    continue

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
                                    key=input("     继续购买请按N，退出请按L\n\t\t")
                                    if key == "N":
                                        continue
                                    elif key == "L":
                                        break
                        #     break
                        # break  

                    elif choice=="2":

                        while True:
                            #清屏
                            os.system("cls")
                            #游戏内容展示
                            print("****************************************")
                            print("            1.石头剪刀布")
                            print("            2.老虎棒子鸡")
                            print("            3.猜数字")
                            print("****************************************")
                            choice = input("请输入您的选项(按R键返回主菜单)：")

                            if choice == "R":

                                print("即将返回主页菜单")
                                time.sleep(1)
                                break

                            elif choice =="1":

                                while True:
                                    os.system("cls")
                                    a=int(input("请输入 1：石头 2：剪刀 3：布\n"))
                                    b=int(random.randint(1,3))

                                    if a==1 and b==1:
                                        print("用户：石头")
                                        print("系统：石头")
                                        print("\n")
                                        print("平局")
                                        key=input("重开请按N，退出请按L")
                                        if key == "N":
                                            continue
                                        elif key == "L":
                                            break

                                    elif a==1 and b==2:
                                        print("用户：石头")
                                        print("系统：剪刀")
                                        print("\n")
                                        print("恭喜您获胜！")
                                        key=input("重开请按N，退出请按L")
                                        if key == "N":
                                            continue
                                        elif key == "L":
                                            break 
                                        
                                    elif a==1 and b==3:
                                        print("用户：石头")
                                        print("系统：布")
                                        print("\n")
                                        print("不好意思，您输了") 
                                        key=input("重开请按N，退出请按L")
                                        if key == "N":
                                            continue
                                        elif key == "L":
                                            break
                                        
                                    elif a==2 and b==1:
                                        print("用户：剪刀")
                                        print("系统：石头")
                                        print("\n")
                                        print("不好意思，您输了")
                                        key=input("重开请按N，退出请按L")
                                        if key == "N":
                                            continue
                                        elif key == "L":
                                            break 
                                        
                                    elif a==2 and b==2:
                                        print("用户：剪刀")
                                        print("系统：剪刀")
                                        print("\n")
                                        print("平局")  
                                        key=input("重开请按N，退出请按L")
                                        if key == "N":
                                            continue
                                        elif key == "L":
                                            break
                                        
                                    elif a==2 and b==3:
                                        print("用户：剪刀")
                                        print("系统：布")
                                        print("\n")
                                        print("恭喜您获胜！")  
                                        key=input("重开请按N，退出请按L") 
                                        if key == "N":
                                            continue
                                        elif key == "L":
                                            break
                                        
                                    elif a==3 and b==1:
                                        print("用户：布")
                                        print("系统：石头")
                                        print("\n")
                                        print("恭喜您获胜！") 
                                        key=input("重开请按N，退出请按L")
                                        if key == "N":
                                            continue
                                        elif key == "L":
                                            break
                                        
                                    elif a==3 and b==2:
                                        print("用户：布")
                                        print("系统：剪刀")
                                        print("\n")
                                        print("不好意思，您输了")  
                                        key=input("重开请按N，退出请按L")
                                        if key == "N":
                                            continue
                                        elif key == "L":
                                            break
                                        
                                    elif a==3 and b==3:
                                        print("用户：布")
                                        print("系统：布")
                                        print("\n")
                                        print("平局")   
                                        key=input("重开请按N，退出请按L")
                                        if key == "N":
                                            continue
                                        elif key == "L":
                                            break

                                    else:
                                        print("\n\n\n") 
                                        print("您输入有误")
                            elif choice == "2":

                                while True:

                                    os.system("cls")
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
                                            key=input("重开请按N，退出请按L")
                                            if key == "N":
                                                continue
                                            elif key == "L":
                                                break

                                        elif(animal==1 and num==2)or\
                                            (animal==2 and num==4)or\
                                            (animal==3 and num==1)or\
                                            (animal==4 and num==3):

                                            print("系统输出：",num1)
                                            print("你可真菜。。")
                                            key=input("重开请按N，退出请按L")
                                            if key == "N":
                                                continue
                                            elif key == "L":
                                                break
                                        else:

                                            print("系统输出：",num1)
                                            print("en棋逢对手啊·不错不错")
                                            key=input("重开请按N，退出请按L")
                                            if key == "N":
                                                continue
                                            elif key == "L":
                                                break

                                    pass
                            elif choice == "3":

                                while True:

                                    os.system("cls")
                                    range1=int(input("请输入本局游戏的最小值："))
                                    range2=int(input("请输入本局游戏的最大值："))
                                    num=random.randint(range1,range2)

                                    guess="guess"
                                    n=0

                                    while guess!=num:
                                        n+=1
                                        guess=int(input("请输入你猜的数字："))
                                        if guess<num:
                                            print("您猜的数小了...")
                                            
                                        elif guess>num:       
                                            print("您猜的数大了...")
                                            
                                    else:
                                        print("恭喜您猜对了")
                                        print("您一共猜了",n,"次哦！")
                                        
                                        if n==1:
                                            integral=10
                                        elif n==2:
                                            integral=8
                                        elif n==3:
                                            integral=6
                                        elif n==4:
                                            integral=4
                                        elif n==5:
                                            integral=2
                                        else:
                                            integral=0
                                        print("您的积分为：",integral,"分")
                                        key=input("重开请按N，退出请按L")
                                        if key == "N":
                                            continue
                                        elif key == "L":
                                            break
                            else:
                                print("输入有误，请重新输入")
                                time.sleep(1)
                                continue
                            
                    elif choice=="3":
                        print("客官请慢走....")
                        sys.exit(1)
                        break
                    elif choice == "R":
                        break
                    
                    else:
                        print("输入有误，请重新输入")
                        time.sleep(1)
                        continue
                break                                                

            break

        else:
            print("用户或密码错误，请重新输入")
            time.sleep(2)
            continue
            
    elif a==3:
        print("谢谢光临")
        break
    else:
        print("请重新输入")
        time.sleep(1)
        # continue