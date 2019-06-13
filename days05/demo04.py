'''
用户登录，优化操作
'''
# 引入清屏模块、退出模块，时间操作模块
import os, sys, time

# 定义一个变量，存储多个用户数据

users = [["wu","123"]]
# 展示登录菜单
while True:
    os.system('cls')
    print("\t\t登录菜单")
    print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")
    print("\t\t1. 用户登录")
    print("\t\t2. 新用户注册")
    print("\t\t3. 退出系统")
    print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")

    # 用户输入选项
    choice = input("请输入您的选项：")

    # 判断跳转
    if choice == "1":
        # 用户登录
        while True:
            is_ok = True
            # 请输入账号+密码
            username = input("请输入您的账号(按R键返回登录)：")
            if username == "R":
                is_ok = False
                break
            password = input("请输入您的密码(按R键返回登录)：")
            if password == "R":
                is_ok = False
                break

            # 判断账号密码是否正确
            for user in users:
                if username == user[0] and password == user[1]:
                    # 登录成功
                    print("登录成功，即将即进入首页菜单")
                    is_ok = True
                    break
            else:
                print("账号或者密码有误，请重新操作")
                continue

        if is_ok:
            break
        else:
            continue
        
        # 展示首页菜单
        while True:
            print("\t\t系统首页")
            res = input("按任意键退出系统(R键返回登录).....")
            if res == "R":
                break
            else:
                sys.exit(1)
    
    elif choice == "2":
        pass

    elif choice == "3":
        pass
    
    else:
        print("没有这个选项，请检查后重新操作")
        time.sleep(1)
        continue
