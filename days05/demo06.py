import os,sys,time,random

users=[
    ["wu","q","123",0],
    ["qq","w","123",0]
]

while True:
    os.system("cls")
    print("111111111111111111111111111111111111111111")
    print("            1.用户注册")
    print("            2.用户登录")
    print("            3.退出系统")
    print("            4.你点一下啊")
    print("111111111111111111111111111111111111111111")
    choice = input("      请输入选项：")

    if choice == "1":
        while True:
            os.system("cls")
            accont = input("请输入账号：")

            is_ok = True
            for user in users:
                if accont == user[0]:
                    print("您的账号已经存在，请其他其他账号注册")
                    time.sleep(1)
                    is_ok = False
                # 如果账号已经被使用~开关变量False-> not False-> True
            if not is_ok:
                continue

            username = input("请输入昵称：")
            passwd = input("请输入密码：")
            c_passwd = input("请重新输入密码：")

            if passwd != c_passwd:
                print("两次输入密码不一致，请重新输入：")
                time.sleep(1)
                continue
            elif accont == "" or username == "" or c_passwd == "" or passwd == "":
                print("您输入的信息不能为空，请重新输入：")
                time.sleep(1)
                continue
            else:
                user = [accont,username,passwd]
                users.append(user)
                print("Congratulations， 注册成功,请使用新账号登录.")
                time.sleep(2)
                break

    elif choice == "2":
        while True:

            is_ok = True

            accont = input("         请输入账号：")

            if accont == "":
                print("\t账号不能为空，请重新输入：")
                time.sleep(1)
                break

            passwd = input("         请输入密码：")

            if passwd == "":
                print("\t密码不能为空，请重新输入：")
                time.sleep(1)
                break

            for user in users:

                if accont == user[0] and passwd == user[2]:
                    print("      \n        登录成功")
                    print("      \n   即将跳转用户界面.....")
                    time.sleep(2)
                    is_ok = True
                    break
            else:
                print("您输入的账号或密码错误，请重新输入：")
                time.sleep(1)
                continue
            
            if is_ok:
                break
            else:
                continue
    
        while True:
            os.system("cls")
            print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
            print("             1.购物商城")
            print("             2.休闲小游戏")
            print("             3.返回上级菜单")
            print("             4.修改信息")
            print("             5.积分充值与查询")
            print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
            print("         点击任意键继续：")
            print("\n\n\n\n")

            choice=input("请输入选项（按R键返回主菜单）：")

            if choice == "1":

                while True:
                    os.system("cls")
                    #商品展示
                    print("           欢迎",user[1],"光临")
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
                        
                    id=int(input("\t请选择需要购买的商品："))

                    if id>len(arr):
                        print("\t無商品")

                    else:
                        num=float(input("\t请选择购买商品的数量："))

                        residue=arr[int(id)-1][3]-num

                        # 商品库存
                        # print("sssss",residue)

                        sum=arr[int(id)-1][2]*num

                        credit = sum//10

                        user[3] += credit

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
                            print("\t商品名称：",arr[id-1][1])
                            print("\t商品单价：",arr[id-1][2])
                            print("\t商品个数：",num)
                            print("\t应付金额：",sum)
                            print("\t实付金额：",pay)
                            print("\t找零:     ",pay-sum)
                            print("\t获得积分：",credit)                            
                            print("~*~*~*~*~*~**~*~*~*~*~*~~*~*~*~*~**~~*")
                            key=input("     继续购买请按N，退出请按L\n\t\t")
                            if key == "N":
                                continue
                            elif key == "L":
                                break

            elif choice == "2":
               
                
                while True:
                    if user[3]<=0:
                        print("您的积分不足....")
                        input("按任意键结束")
                        break
                    else:
                        pass
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
                            print("**************************************")
                            print("    赢：积分+1  平局：积分+0 输：积分-1")
                            a=int(input("请输入 1：石头 2：剪刀 3：布\n"))

                            b=int(random.randint(1,3))

                            if a==1 and b==1:
                                print("用户：石头")
                                print("系统：石头")
                                print("\n")
                                print("平局")
                                print("积分+0")
                                user[3] -= 1
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
                                print("积分+1")
                                user[3] += 1
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
                                print("积分-1")
                                user[3] -= 1
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
                                print("积分-1")
                                user[3] -= 1
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
                                print("积分+0")
                                user[3] -= 0
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
                                print("积分+1") 
                                user[3] += 1
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
                                print("积分+1") 
                                user[3] += 1
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
                                print("积分-1") 
                                user[3] -= 1
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
                                print("积分+0") 
                                user[3] += 0
                                if key == "N":
                                    continue
                                elif key == "L":
                                    break

                            else:
                                print("\n\n\n") 
                                print("您输入有误")  
                                continue  

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
                                    print("积分+1") 
                                    user[3] += 1
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
                                    print("积分-1") 
                                    user[3] -= 1
                                    if key == "N":
                                        continue
                                    elif key == "L":
                                        break
                                else:

                                    print("系统输出：",num1)
                                    print("客官，要不要在玩一局")
                                    print("积分+0") 
                                    user[3] += 0
                                    key=input("重开请按N，退出请按L")
                                    if key == "N":
                                        continue
                                    elif key == "L":
                                        break

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
                                user[3] += integral
                                key=input("重开请按N，退出请按L")
                                if key == "N":
                                    continue
                                elif key == "L":
                                    break

                    else:
                        print("\t您输入有误请重新输入：")
                        time.sleep(1)
                        continue

            elif choice == "3":
                time.sleep(1)
                break
            
            elif choice == "4":
                while True:
                    os.system("cls")

                    print("####################")
                    print("    1.修改昵称")
                    print("    2.修改密码")
                    print("####################")
                    choice=input("请选择:")
                    if choice == "1":
                        accont = input("\t请输入您要修改的昵称：")
                        user[1]=accont
                        print("\t修改成功")
                        time.sleep(2)
                        break
                    elif choice == "2":
                        passwd = input("\t请输入您要修改的密码：")
                        user[2] = passwd
                        print("\t修改成功")
                        break
                        
                    else:
                        continue

            elif choice == "5":
                while True:
                    os.system("cls")
                    print("#####################")
                    print("    1.积分查询")
                    print("    2.积分充值")
                    print("    3.返回上一级")
                    print("#####################")
                    choice = input("   请选择：")
                    if choice == "1":
                        print("您的积分为：",user[3])
                        input("按回车继续···")
                        time.sleep(1)
                        continue
                    elif choice == "2":

                        while True:
                            os.system("cls")
                            a = int(input("您要充值的积分："))
                            user[3] += a
                            print("请充值：",a)
                            pay = int(input("请输入金额："))
                            
                            if pay < a:
                                print("金额不足无法充值")
                                a=input("按任意键再次充值,按R键退出充值")
                                if a=="R":
                                    break
                                continue
                            else:
                                print("您充值的积分为：",a)
                                print("您的可用积分为：",user[3])
                                print("找零：",pay-a)
                                print("**************************")
                                print("**************************")
                                input("按任意键结束....")
                                continue

                            break

                    elif choice == "3":
                        break


            else:
                print("\t您输入有误，请重新输入：")
                continue
            
            

    elif choice == "3":
        print("\t4s 后退出...")
        time.sleep(1)
        print("\t3s 后退出...")
        time.sleep(1)
        print("\t2s 后退出...")
        time.sleep(1)
        print("\t1s 后退出...")
        time.sleep(1)

    elif choice == "4":
        print("\t让你点你就点啊，点完你就是我的人了")
        print("\thhhhhhhhhhhhhha")
        input("\t你再点一下")
        continue

    else:
        print("没有此选项，请重新输入：")
        time.sleep(1)
        continue
