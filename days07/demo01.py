'''

'''
users = dict()
user = {"user_name":"wu","passwd":"123"}

while True:
    print("**********************************************")
    print("                    1.用户登录")
    print("                    2.用户注册")
    print("                    3.退出系统")
    print("**********************************************")

    choice = input("请输入选项：")
    if choice == "1":
        while True:

            user_name = input("用户名：")
            passwd = input("密码：")
            if user_name in users and passwd == users[user_name]["passwd"]:
                input("登陆成功")
            else:
                input("用户或密码错误")
                break
            a = input("按r键返回")
            if a == "r":
                break
            else:
                continue



    elif choice == "2":
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
            user = {"user_name":user_name,"passwd":passwd}
            users[user_name] = user
            print("注册成功")
            print(user)
            print((users))
            break
    elif choice == "3":
        pass
    else:
        input("输入有误，请重新输入：")
        continue