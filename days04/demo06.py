'''
菜单的上下级跳转
    上级菜单[进入下级菜单]
        下级菜单[返回上一级菜单]
'''
# os-操作系统 sys-解释器 time-时间
import os, sys, time

# 展示首页菜单
while True:
    os.system('cls')
    print("\t\tPY1901电商平台首页")
    print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")
    print("\t\t1. 进入购物超市")
    print("\t\t2. 休闲小游戏")
    print("\t\t3. 返回登录菜单")
    print("\t\t4. 退出系统")
    print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")
    
    # 用户输入选项
    choice = input("请输入您的选项：")

    if choice == "1":
        # 展示购物超市菜单
        while True:
            os.system('cls')
            print("\t\tPY1901购物超市")
            print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")
            print("商品名称\t商品单价\t商品库存\t商品产地\t商品描述")
            print("暂时没有商品上架")
            print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")
            
            # 用户输入选项
            choice = input("请输入您要购买的商品编号(按R键返回主菜单)：")

            # 判断用户的输入并跳转到不同菜单
            if choice == "R":
                print("即将返回主页菜单")
                time.sleep(1)
                break
            else:
                print("功能正在升级中...请重新操作")
                time.sleep(1)
                continue
    
    elif choice == "2":
        # 展示休闲小游戏菜单
        while True:
            os.system('cls')
            print("\t\tPY1901电商平台小游戏")
            print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")
            print(" 休闲小游戏，休闲又放松，同时挣积分")
            print("\t\t1. 石头剪刀布")
            print("\t\t2. 老虎棒子鸡")
            print("\t\t3. 猜数字")
            print("\t\t4. 返回主页菜单")
            print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")

            # 提示用户输入选项
            choice = input("请输入您的选项(按R键返回主菜单)：")

            if choice == "R":
                print("即将返回主页菜单")
                time.sleep(1)
                break
            else:
                print("功能正在升级中，请返回重新操作....")
                time.sleep(1)
                continue

    elif choice == "3":
        pass

    elif choice == "4":
        print("客官慢走....3S后系统退出....")
        time.sleep(1)
        print("客官慢走....2S后系统退出....")
        time.sleep(1)
        print("客官慢走....1S后系统退出....")
        time.sleep(1)
        sys.exit(1)
    else:
        input("没有这个选项，按任意键继续")
        continue