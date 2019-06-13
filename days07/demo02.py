'''

'''
import time ,os ,random

users = {"wu":{"user_name":"wu","passwd":"123","sorce":100,"accont":"rose"}}
user = {"user_name":"wu","passwd":"123","sorce":100}

while True:
    print("                   Shopping Market")
    print("**********************************************")
    print("                    1.用户登录")
    print("                    2.用户注册")
    print("                    3.退出系统")
    print("**********************************************")

    choice = input("              请输入选项：")
    if choice == "1":
        while True:

            user_name = input("用户名：")
            passwd = input("密码：")
            if user_name in users and passwd == users[user_name]["passwd"]:
                input("登陆成功")
                break
            else:
                a = input("用户或密码错误，按任意键继续（按r返回登录界面）")
                continue
        while True:
            print("############################")
            print("          欢迎", users[user_name]["accont"], "光临")
            print("############################")
            print("           1.购物商城")
            print("           2.休闲小游戏")
            print("           3.返回上级菜单")
            print("           4.修改信息")
            print("           5.积分充值与查询")
            print("############################")
            print("\n")
            choice = input("      请输入选项:")
            if choice == "1":
                while True:
                    # print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
                    # print("商品编号\t商品名称\t商品单价\t商品库存\t商品描述")
                    # print("1\t\t苹果\t\t5.00\t\t80\t\t又大又甜")
                    # print("2\t\t橘子\t\t4.00\t\t80\t\t不甜不要钱")
                    # print("3\t\t芒果\t\t8.00\t\t80\t\t味美多汁")
                    # print("4\t\t榴莲\t\t43.00\t\t80\t\t跟屎一样香")
                    good1 = {"id": 1, "good_name": "apple", "good_price": 4, "repertory": 80, "describe": "又大又甜"}
                    good2 = {"id": 2, "good_name": "orange", "good_price": 4, "repertory": 80, "describe": "不甜不要钱"}
                    good3 = {"id": 3, "good_name": "mango", "good_price": 8, "repertory": 80, "describe": "味美多汁"}
                    good4 = {"id": 4, "good_name": "durian", "good_price": 43, "repertory": 80, "describe": "跟屎一样香"}
                    shop = {1:good1,2:good2,3:good3,4:good4}
                    print(shop)

                    choice = int(input("请输入要购买的商品编号"))

                    if choice in shop.keys():
                        num = int(input("请输入要购买的数量："))
                        residue = shop[choice]["repertory"] - num
                        sum = shop[choice]["good_price"]* num
                        credit = sum //10
                        users[user_name]["sorce"] += credit
                        print("\t您需要支付",sum,"元")
                        pay = int(input("\t实付金额："))
                        print("\n")
                        input("\t点击任意键结算....")

                        if pay < sum:
                            print("\terror")
                            print("请您付全款，谢谢")
                            time.sleep(2)
                            continue

                        else:
                            os.system("cls")
                            print("~*~*~*~*~*~**~*~*~*~*~*~~*~*~*~*~**~~*")
                            print("\t商品名称：",shop[choice]["good_name"])
                            print("\t商品单价：",shop[choice]["good_price"])
                            print("\t商品个数：", num)
                            print("\t应付金额：", sum)
                            print("\t实付金额：", pay)
                            print("\t找零:     ", pay - sum)
                            print("\t获得积分：", credit)
                            print("~*~*~*~*~*~**~*~*~*~*~*~~*~*~*~*~**~~*")
                            key = input("     继续购买请按N，退出请按L\n\t\t")
                            if key == "N":
                                continue
                            elif key == "L":
                                break




            elif choice == "2":
                while True:
                    if users[user_name]["sorce"] <= 0:
                        print("您的积分不足....")
                        input("按任意键结束")
                        break
                    else:
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

                        elif choice == "1":

                            while True:

                                print("**************************************")
                                print("    赢：积分+1  平局：积分+0 输：积分-1")
                                a = int(input("请输入 1：石头 2：剪刀 3：布\n"))

                                b = int(random.randint(1, 3))

                                if a == 1 and b == 1:
                                    print("用户：石头")
                                    print("系统：石头")
                                    print("\n")
                                    print("平局")
                                    print("积分+0")
                                    users[user_name]["sorce"] -= 1
                                    key = input("重开请按N，退出请按L")
                                    if key == "N":
                                        continue
                                    elif key == "L":
                                        break

                                elif a == 1 and b == 2:
                                    print("用户：石头")
                                    print("系统：剪刀")
                                    print("\n")
                                    print("恭喜您获胜！")
                                    print("积分+1")
                                    users[user_name]["sorce"] += 1
                                    key = input("重开请按N，退出请按L")
                                    if key == "N":
                                        continue
                                    elif key == "L":
                                        break

                                elif a == 1 and b == 3:
                                    print("用户：石头")
                                    print("系统：布")
                                    print("\n")
                                    print("不好意思，您输了")
                                    print("积分-1")
                                    users[user_name]["sorce"] -= 1
                                    key = input("重开请按N，退出请按L")
                                    if key == "N":
                                        continue
                                    elif key == "L":
                                        break

                                elif a == 2 and b == 1:
                                    print("用户：剪刀")
                                    print("系统：石头")
                                    print("\n")
                                    print("不好意思，您输了")
                                    print("积分-1")
                                    users[user_name]["sorce"] -= 1
                                    key = input("重开请按N，退出请按L")
                                    if key == "N":
                                        continue
                                    elif key == "L":
                                        break

                                elif a == 2 and b == 2:
                                    print("用户：剪刀")
                                    print("系统：剪刀")
                                    print("\n")
                                    print("平局")
                                    print("积分+0")
                                    users[user_name]["sorce"] -= 0
                                    key = input("重开请按N，退出请按L")
                                    if key == "N":
                                        continue
                                    elif key == "L":
                                        break

                                elif a == 2 and b == 3:
                                    print("用户：剪刀")
                                    print("系统：布")
                                    print("\n")
                                    print("恭喜您获胜！")
                                    print("积分+1")
                                    users[user_name]["sorce"] += 1
                                    key = input("重开请按N，退出请按L")
                                    if key == "N":
                                        continue
                                    elif key == "L":
                                        break

                                elif a == 3 and b == 1:
                                    print("用户：布")
                                    print("系统：石头")
                                    print("\n")
                                    print("恭喜您获胜！")
                                    print("积分+1")
                                    users[user_name]["sorce"] += 1
                                    key = input("重开请按N，退出请按L")
                                    if key == "N":
                                        continue
                                    elif key == "L":
                                        break

                                elif a == 3 and b == 2:
                                    print("用户：布")
                                    print("系统：剪刀")
                                    print("\n")
                                    print("不好意思，您输了")
                                    print("积分-1")
                                    users[user_name]["sorce"] -= 1
                                    key = input("重开请按N，退出请按L")
                                    if key == "N":
                                        continue
                                    elif key == "L":
                                        break

                                elif a == 3 and b == 3:
                                    print("用户：布")
                                    print("系统：布")
                                    print("\n")
                                    print("平局")
                                    key = input("重开请按N，退出请按L")
                                    print("积分+0")
                                    users[user_name]["sorce"] += 0
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
                                num = random.randint(1, 4)
                                num = int(num)
                                print("请输入您选择的动物：")
                                animal = int(input("1.老虎 2.棒子 3.鸡 4.虫子\n"))

                                if num == 1:
                                    num1 = "老虎"

                                elif num == 2:
                                    num1 = "棒子"

                                elif num == 3:
                                    num1 = "鸡"

                                elif num == 4:
                                    num1 = "虫子"

                                if animal > 4:
                                    print("输入有误")

                                else:

                                    if (animal == 1 and num == 3) or \
                                            (animal == 2 and num == 1) or \
                                            (animal == 3 and num == 4) or \
                                            (animal == 4 and num == 2):

                                        print("系统输出：", num1)
                                        print("可把你牛逼坏了")
                                        print("积分+1")
                                        users[user_name]["sorce"] += 1
                                        key = input("重开请按N，退出请按L")
                                        if key == "N":
                                            continue
                                        elif key == "L":
                                            break

                                    elif (animal == 1 and num == 2) or \
                                            (animal == 2 and num == 4) or \
                                            (animal == 3 and num == 1) or \
                                            (animal == 4 and num == 3):

                                        print("系统输出：", num1)
                                        print("你可真菜。。")
                                        key = input("重开请按N，退出请按L")
                                        print("积分-1")
                                        users[user_name]["sorce"] -= 1
                                        if key == "N":
                                            continue
                                        elif key == "L":
                                            break
                                    else:

                                        print("系统输出：", num1)
                                        print("客官，要不要在玩一局")
                                        print("积分+0")
                                        users[user_name]["sorce"] += 0
                                        key = input("重开请按N，退出请按L")
                                        if key == "N":
                                            continue
                                        elif key == "L":
                                            break
                        elif choice == "3":

                            while True:

                                os.system("cls")
                                range1 = int(input("请输入本局游戏的最小值："))
                                range2 = int(input("请输入本局游戏的最大值："))
                                num = random.randint(range1, range2)

                                guess = "guess"
                                n = 0

                                while guess != num:
                                    n += 1
                                    guess = int(input("请输入你猜的数字："))
                                    if guess < num:
                                        print("您猜的数小了...")

                                    elif guess > num:
                                        print("您猜的数大了...")

                                else:
                                    print("恭喜您猜对了")
                                    print("您一共猜了", n, "次哦！")

                                    if n == 1:
                                        integral = 10
                                    elif n == 2:
                                        integral = 8
                                    elif n == 3:
                                        integral = 6
                                    elif n == 4:
                                        integral = 4
                                    elif n == 5:
                                        integral = 2
                                    else:
                                        integral = 0
                                    print("您的积分为：", integral, "分")
                                    users[user_name]["sorce"] += integral
                                    key = input("重开请按N，退出请按L")
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


                    print("####################")
                    print("    1.修改昵称")
                    print("    2.修改密码")
                    print("    3.返回上一级")
                    print("####################")
                    choice = input("请选择:")
                    if choice == "1":
                        accont = input("\t请输入您要修改的昵称：")
                        users[user_name]["accont"] = accont
                        print("\t修改成功")
                        time.sleep(2)
                        break
                    elif choice == "2":
                        while True:
                            passwd = input("\t请输入您的密码：")
                            if passwd == users[user_name]["passwd"]:
                                new_passwd = input("请输入新的密码")
                                c_new_passwd = input("请重新输入密码")
                                if new_passwd ==c_new_passwd:
                                    users[user_name]["passwd"] = c_new_passwd
                                    print("修改成功")
                                    break
                                else:
                                    continue
                    elif choice == "3":
                        break

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
                        print("您的积分为：", users[user_name]["sorce"])
                        input("按回车继续···")
                        time.sleep(1)
                        continue
                    elif choice == "2":

                        while True:

                            a = int(input("您要充值的积分："))
                            users[user_name]["sorce"] += a
                            print("请充值：", a)
                            pay = int(input("请输入金额："))

                            if pay < a:
                                print("金额不足无法充值")
                                a = input("按任意键再次充值,按R键退出充值")
                                if a == "R":
                                    break
                                continue
                            else:
                                print("您充值的积分为：", a)
                                print("您的可用积分为：", users[user_name]["sorce"])
                                print("找零：", pay - a)
                                print("**************************")
                                print("**************************")
                                input("按任意键结束....")
                                continue

                            break

                    elif choice == "3":
                        break

            else:
                input("没有此选项，按任意键重新输入")
                continue


    elif choice == "2":
        while True:
            user_name = input("请输入用户名：")
            if user_name in users:
                input("用户名已存在，请重新输入：")
                continue
            passwd = input("请输入密码：")
            c_passwd = input("请再次输入密码：")
            accont = input("请输入昵称：")
            if passwd != c_passwd:
                print("两次输入密码不一致，请重新输入：")
                continue
            user = {"user_name":user_name,"passwd":passwd,"sorce":100,"accont":accont}
            users[user_name] = user
            print("注册成功")
            print(user)
            print((users))
            break
    elif choice == "3":

        print("系统将在3s后退出.....")
        time.sleep(1)
        print("系统将在2s后退出.....")
        time.sleep(1)
        print("系统将在2s后退出.....")
        time.sleep(1)

    else:
        input("输入有误，请重新输入：")
        continue