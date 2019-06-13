import os, sys, time, random

goods = []
bag = [["西红柿",1],\
        ["番茄",2]
]

store = []

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
            print("              3.查看自己的小仓库")
            print("              4.查看蛙儿子的背包")
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
                    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                    print("\n")
                    shop = [
                        {"id": 1, "good_name": "西紅柿", "good_price": 10},
                        {"id": 2, "good_name": "番茄\t", "good_price": 12},
                        {"id": 3, "good_name": "土豆\t", "good_price": 15},
                        {"id": 4, "good_name": "黄瓜\t", "good_price": 17},
                        {"id": 5, "good_name": "青椒\t", "good_price": 14},
                    ]

                    for good in shop:
                        print("编号:%s 商品  %s 价格  %s" % (good["id"], good["good_name"], good["good_price"]))

                    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

                    choice = int(input("请输入购买编号："))

                    if choice > len(shop):

                        print("无商品")

                    else:
                        for id in shop:
                            if choice == id["id"]:
                                print(id["good_name"])
                                a = id["good_price"]
                        num = int(input("请输入要购买的数量："))
                        sum = a * num
                        if user[2] < sum:
                            print("您的金币不足")
                            time.sleep(1)
                            break
                        else:
                            balance = user[2] - sum
                            user[2] -= sum
                            # good = arr[choice][1]
                            # article = [good, num]
                            # store.append(article)

                            print("     您本次购买的商品是:", good["good_name"])
                            print("     您本次消费金币为： ", sum, )
                            print("     您的金币还有:\t", balance)
                            key = input("     继续购买请按N，退出请按L\n\t\t")
                            if key == "N":
                                sum = 0
                                continue
                            elif key == "L":
                                break


            elif choice == "3":

                while True:
                    os.system("cls")

                    for i in range(len(store)):
                        for j in range(len(store[0])):
                            print(store[i][j],end = "\t")
                        print("\r\n")
                                                                             
                    print("##########################################")
                    print("          1.往背包中添加东西")
                    print("          2.返回上一界面")
                    print("##########################################")
                    choice = input("请输入选项：")

                    if choice == "1":
                        
                        a = input("请输入要添加的东西：")
                        for i in range(len(store)):
                            if store[i][0] == a:
                                print(i)
                                break

                        print(store[i][0],"还有",store[i][1],"个")
                        b = int(input("请输入要添加的数量："))
                        if b > store[i][1]:
                            print("商品不足，请重新输入")
                            break
                        else:
                            store [i][1] -= b
                            goods = [a,b]
                            bag.append(goods)
                            print(store[i][0],"还有",store[i][1],"个")
                            c = input("继续添加请按c,返回请按l:\n")
                            if c == "c":
                                continue
                            elif c == "l":
                                break
                            else:
                                print("输入有误，请重新输入：")
                                continue
                        break

                    if choice == "2":
                        print("即将返回上一级")
                        time.sleep(1)
                        break
                    else:
                        a = input("没有此选项，请重新输入(按r键返回)\n")
                        if a == "r":
                            time.sleep(1)
                            break
                        else:
                            time.sleep(1)
                            continue                                          

            elif choice == "4":
                
                while True:
                    os.system("cls")

                    for i in range(len(bag)):
                        for j in range(len(bag[0])):
                            print(bag[i][j],end="\t")
                        print("\r\n")
                    input("安任意键返回")
                    break


            elif choice == "5":
                while True:
                    a = random.randint(1,10)
                    times = 3
                    if bag == "":
                        print("背包没有食物了，蛙儿子饿坏了")
                        time.sleep(1)
                        times -= 1
                    else:
                        if 1 <= a <= 3:
                            
                            print("咦？我蛙儿子呢？又出去玩去了，回来再收拾他")
                            food = random.choice(bag)
                            de = bag.remove(food)
                            print(food)
                            print(de)
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