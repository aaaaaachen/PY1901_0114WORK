import os,sys,time,random

goods = []
bag = [["西红柿",1],\
        ["番茄",2]
]
goodss = []
food = []
users = [
    ["wu","123",0,goods],
    ["wz","123",0,goods]
]

num = 3
sum = 0

while True:
    os.system("cls")
    print("*******************************")
    print("         旅行青蛙")
    print("*******************************")
    print("\t")
    print("        1.用户登录")
    print("        3.用户注册")
    print("        4.退出游戏")
    print("\t")
    print("*******************************")
    choice = input("\t请输入选项：")
    if choice == "1":

        while True:
            os.system("cls")
            is_ok = True
            account = input("请输入账号：")

            if account == "":
                print("您输入的账号不能为空，请重新输入")
                time.sleep(1)
                continue

            passwd = input("请输入密码：")

            if passwd == "":
                print("您输入的密码不能为空，请重新输入")
                time.sleep(1)
                continue

            for user in users:
                
                if user[0] == account and user[1] == passwd:
                    print("登录成功")
                    is_ok = True
                    break
            else:
                print("您输入的账号或密码有误，请重新输入：")
                is_ok = False
                continue
            if is_ok:
                break
            else:
                continue

        while True:
            os.system("cls")
            print("""""""""""""""""""""""""""""""""""""""""""""""""")
            print("              1.收集金币")
            print("              2.购物商城")
            print("              3.查看背包中的物品")
            print("              4.给蛙儿子准备生活用品")
            print("              5.查看蛙儿子在干啥")
            print("              6.返回上级界面")
            print("""""""""""""""""""""""""""""""""""""""""""""""""")

            choice = input("\t请输入选项：")

            if choice == "1":
                
                while True:
                    is_ok = True
                    # money = random.randint(10,100)
                    if num <=0:
                        print("您的机会以用完....")
                        print("您的金币总数为：",user[2])
                        input("按任意键返回")
                        time.sleep(1)
                        break
                    else:
                        money = random.randint(10,100)
                        num -= 1
                        user[2] += money
                        print("剩余次数",num)
                        print("收集的金币个数：",money)
                        
                        a = input("点击任意键继续(点击r键终止收集)")
                        
                        if a == "r":
                            print("您的金币总数为：",user[2])
                            input("按任意键返回")
                            time.sleep(1)
                            break
                        continue
             
            elif choice == "2":
                while True:
                    os.system("cls")
                    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                    print("\n")
                    arr = [
                            ["编号","商品\t","价格"],\
                            [1,"西红柿\t",12],\
                            [2,"番茄\t",15],\
                            [3,"蛋炒饭\t",20],\
                            [4,"红烧排骨",50],\
                            [5,"被子\t",90],\
                            [6,"帐篷\t",120]
                    ]
                    for i  in  range(len(arr)):
                        for j in range(len(arr[0])):
                            print(arr[i][j],end="\t\t")
                        print("\r\n")
                    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")


                    choice = int(input("请输入购买编号："))

                    if choice > len(arr)-1:

                        print("无商品")

                    else:
                        num = int(input("请输入要购买的数量："))
                        sum = arr[choice][2]*num
                        if user[2] < sum:
                            print("您的金币不足")
                            time.sleep(1)
                            break
                        else:
                            balance=user[2]-sum
                            user[2]-=sum
                            good = arr[choice][1]
                            article = [good,num]
                            # for i in range(len(article)):
                            #     print(article[i],end="\t")
                            goods.append(article)
                            user[3].append(goods)
                                
                            print("     您本次购买的商品是:",good)
                            print("     您本次消费金币为： ",sum,)
                            print("     您的金币还有:\t",balance)
                            key=input("     继续购买请按N，退出请按L\n\t\t")
                            if key == "N":
                                sum=0
                                continue
                            elif key == "L":
                                break

            elif choice == "3":
                for i in range(len(goods)):
                    print(goods[i],end="")
                # print(goods)
                # print("\r\n") 
                           
                input("按任意键返回")
                continue
            elif choice == "4":

                # bag.extend(food)

                for i in range(len(bag)):
                    for j in range(len(bag[0])):
                        print(bag[i][j],end="\t")
                    print("\r\n")
                a = input("请输入背包的食物：")
                for i in range(len(bag)):
                    if bag[i][1] == a:
                        print(i)
                        break
                print(bag[i][0],"还有",bag[i][1],"个")
                b = input("输入放入的数量：")
                if b > bag[i][1]:
                    print("背包中数量不足")

                time.sleep(3)



            elif choice == "5":
                while True:
                    a = random.randint(1,10)
                    times = 3
                    if user[3] == "":
                        print("背包没有食物了，蛙儿子饿坏了")
                        time.sleep(1)
                        times -= 1
                    else:
                        if 1 <= a <= 3:
                            print("咦？我蛙儿子呢？又出去玩去了，回来再收拾他")
                            r = input("点击任意键返回")
                            if r == "r":
                                break
                            else:
                                continue
                        elif 3 < a < 6:
                            print("慢点吃，别噎着")
                            r = input("点击任意键返回")
                            if r == "r":
                                break
                            else:
                                continue
                        elif 6 <= a < 8:
                            print("睡得挺香，不打扰你了")
                            r = input("点击任意键返回")
                            if r == "r":
                                break
                            else:
                                continue
                        
                        else:
                            print("不错不错，还知道看书")
                            r = input("点击任意键返回")
                            if r == "r":
                                break
                            else:
                                continue
                        if time <= 0:
                            print("蛙儿子挂了")
                            print("游戏凉了")
                            input("按任意键返回")
                            break
            elif choice == "6":
                print("\t即将返回上一界面")
                time.sleep(2)
                break



    elif choice == "2":

        while True:

            is_ok = True
            print("*********************")
            account = input("\t请输入您要注册的账号：")
            for user in users:
                if account == user[0]:
                    print("您输入的账号已被注册")
                    input("按任意键继续注册")
                    is_ok = False
            if not is_ok:
                continue

            passwd = input("\t请输入您的密码：")
            c_passwd = input("\t请再次输入密码：")
            if passwd != c_passwd:
                print("\t两次输入密码不一致")
                input("\t按任意键重新输入")
                continue
            else:
                user = [account,passwd]
                users.append(user)
                print("恭喜您，您已注册成功")
                time.sleep(1)
                break
        
        # print("*********************")
            




        
    elif choice == "3":
        print("游戏即将退出")
        time.sleep(1)
        exit()
    
    else:
        print("\t没有此选项，请重新操作")
        time.sleep(2)
        continue