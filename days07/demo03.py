'''
	登录菜单
		用户登录
		用户注册
		退出系统
	首页菜单
		个人资料维护
		文章数据维护
		返回上一级
		退出系统
	【个人资料维护】
		修改登录密码
		完善个人资料
		返回上一级
	【文章数据维护】
		发表文章
		查看所有文章
		查看个人文章


'''

import time

users = dict()
user = {"user_name":"wu","passwd":"123"}

#登录界面显示
def show_login():
    print("1.用户登录")
    print("2.用户注册")
    print("3.退出系统")

#首页菜单显示
def show_home_page():
    print("1.个人资料维护")
    print("2.文章数据维护")
    print("3.返回上一级")
    print("4.退出系统")

#个人资料维护
def self_update():
    print("1.修改登录密码")
    print("2.完善个人资料")
    print("3.返回上一级")

#文章资料维护
def essay_update():
    print("1.发表文章")
    print("2.查看所有文章")
    print("3.查看个人文章")


def loading():
    pass


def register():
    while True:
        user_name = input("请输入用户名：")
        if user_name in users:
            input("用户名已存在，请重新输入：")
            continue
        passwd = input("请输入密码：")
        c_passwd = input("请再次输入密码：")
        if passwd != c_passwd:
            print("两次输入密码不一致，请重新输入：")
            continue
        user = {"user_name": user_name, "passwd": passwd}
        users[user_name] = user
        print("注册成功")
        print(user)
        print((users))
        break




while True:
    show_login()
    choice = input("请输入选项：")
    if choice == "1":
        while True:
            show_home_page()
            choice = input("请输入选项：")
            if choice == "1":
                while True:
                    self_update()

                    choice = input("请输入选项")
                    if choice == "1":
                        print("升级中")
                        show_home_page()
                    elif choice == "2":
                        print("升级中")
                        break
                    elif choice == "3":
                        print("升级中")
                        break
                    else:
                        break
            elif choice == "2":
                while True:
                    essay_update()
                    choice = input("请输入选项：")
                    if choice == "1":
                        print("升级中")
                        break
                    elif choice =="2":
                        print("升级中")
                        break
                    elif choice == "3":
                        print("升级中")
                        break
                    else:
                        break
            elif choice == "3":
                break
            elif choice =="4":
                print("即将退出系统")
                exit()
    elif choice == "2":
        print("升级中")
        show_login()
    elif choice == "3":
        print("即将退出")
        time.sleep(1)
        exit()
    else:
        print("输入有误，请重新输入")


