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

users = {"wu":{"user_name":"wu","passwd":"123"}}
user = {"user_name":"wu","passwd":"123","hobby":"basketball","sex":"female","fanifesto":"大帅比"}

#登录界面显示
def show_login():

    print("1.用户登录")
    print("2.用户注册")
    print("3.退出系统")
    choice = input("请输入选项：")
    if choice == "1":
        loading()
    elif choice == "2":
        register()
    elif choice == "3":
        time.sleep(2)
        exit()
    else:
        show_login()

#首页菜单显示


def show_home_page():
    while True:
        print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
        print("        1.个人资料维护")
        print("        2.文章数据维护")
        print("        3.返回上一级")
        print("        4.退出系统")
        print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
        choice = input("请输入选项：")
        if choice == "1":
            self_update()
        elif choice == "2":
            essay_update()
        elif choice == "3":
            time.sleep(2)
            show_login()
        elif choice == "4":
            exit()
        else:
            continue


def loading():
        user_name = input("用户名：")
        if user_name == "r":
           show_login()
        user_passwd = input("密码：")
        if user_name in users and user_passwd == users[user_name]["passwd"]:
            print("登陆成功")
            time.sleep(1)
            return show_home_page()
        else:
            print("用户或密码有误，请重新输入：")
            time.sleep(1)
            return loading()


def register():

    user_name = input("请输入用户名：")
    if user_name in users:
        input("用户名已存在，请重新输入：")
        register()
    passwd = input("请输入密码：")
    c_passwd = input("请再次输入密码：")
    if passwd != c_passwd:
        print("两次输入密码不一致，请重新输入：")
        register()
    user = {"user_name": user_name, "passwd": passwd}
    users[user_name] = user
    print("注册成功")
    print(user)
    print((users))
    show_login()




def update_passwd(user):

    passwd = input("请输入您的密码：")
    if passwd != user["passwd"]:
        print("您输入的密码错误")
        update_passwd(user)
    new_passwd = input("请输入新的密码：")
    c_new_passwd = input("请输入新的密码：")
    if new_passwd == c_new_passwd:
        print("修改成功")
        input("按任意键返回上一级")
        self_update()
    else:
        print("两次输入密码不一致，请重新输入：")
        update_passwd()


# def complete_self_message(user):
#     for i in user:
#         print("%s : %s"%(i,user.get(i)))
#     modify = input("请输入要修改的内容：")
#     if modify == ""






def self_update():

    while True:
        print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
        print("        1.修改登录密码")
        print("        2.完善个人资料")
        print("        3.返回上一级")
        print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
        choice = input("请输入选项：")
        if choice == "1":
            update_passwd(user)
        elif choice == "2":
            complete_self_message(user)
        elif choice == "3":
            show_home_page()
        else:
            continue
#文章资料维护
def essay_update():

    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
    print("         1.发表文章")
    print("         2.查看所有文章")
    print("         3.查看个人文章")
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
    choice = input("请输入选项：")
    if choice == "1":
        print("升级中")
    elif choice == "2":
        print("升级中")
    elif choice == "3":
        print("升级中")
    else:
        show_login()






show_login()

