'''
个人博客面向对象开发
    OOA：首先抽象项目中可能存在的对象
    然后通过对象抽取可能出现的类型【属性/行为】
    OOD：分析属性的必要性，行为的可行性

    用户：user
    系统：通用的Common 核心的Core
    通过函数定义各种登录菜单：
    展示菜单【登录菜单，注册菜单，首页菜单】

    功能：
        系统功能：注册，登录，退出
        用户功能：修改密码，完善资料
'''
import os,time,sys

users = {}
online = None
essays = {}
recyclebin = {}
comment = {}
message1 = {}
email1 ={}
accont = {}



# show_index_menu = {
#     "1":personal_center,
#     "2":essay_center,
#     "3":message_center,
#     "4":show_login,
#     "5":system_exit
# }

# personal_center_menu = {
#     "1":update_passwd,
#     "2":prefect_self_info,
#     "3":show_index
# }
#
# essay_center_menu = {
#     "1":essay_publish,
#     "2":look_essays,
#     "3":look_self_essay,
#     "4":regulate_self_essay,
#     "5":show_index
# }
#
# regulate_self_essay_menu = {
#     "1":update_self_essay,
#     "2":delate_self_essay,
#     "3":recycle_bin,
#     "4":essay_center
# }
#
# recycle_bin_menu = {
#     "1":recover_essay,
#     "2":dela_essay_forever,
#     "3":regulate_self_essay
# }






#定义用户对象
class User:
    def __init__(self,account):
        self.account = account



#定义系统对象
class Core:
    def __init__(self):
        pass



    def show_login(self):

        print("*******************************")
        print("          1.登录")
        print("          2.注册")
        print("          3.退出")
        print("*******************************")

        choice = input("请输入选项：")
        return show_login_menu.get(choice)() if choice in show_login_menu else self.show_login()

    def loading(self):
        print("****************************")
        print("       1.账号密码登录")
        print("       2.邮箱密码登录")
        print("****************************")

        choice = input("请输入选项(R键返回)：")
        # 重新定义全局变量
        global online
        if choice.upper() == "R":
            return self.show_login()
        # 账号密码登录
        elif choice == "1":
            user_name = input("    账号：")
            passwd = input("     密码：")
            if user_name in users and passwd == users[user_name]["passwd"]:
                print("登录成功，即将跳转首页")

                online = users.get(user_name)
                time.sleep(1)
                show_index()
            else:
                print("账户或密码错误，请重新输入：")
                return self.loading()
        # 邮箱密码登录
        elif choice == "2":
            emai = input("请输入邮箱：")
            passwd = input("请输入密码：")
            if emai in email1 and passwd == email1[emai]["passwd"]:
                print("登录成功,即将跳转首页")

                online = email1.get(emai)
                time.sleep(1)
                show_index()
            else:
                print("邮箱或密码错误，请重新输入：")
                return self.loading()
        else:
            return self.loading()

    def register(self):
        user_name = input("请输入账号:")
        if user_name in users:
            print("账号已经存在，请重新注册")
            return self.register()
        passwd = input("请输入密码:")
        c_passwd = input("请再次输入密码")
        email = input("请输入邮箱：")
        nick_name = input("请输入昵称")
        if passwd != c_passwd:
            print("两次输入密码不一致，请重新输入：")
            return self.register()
        print("注册成功")
        user = {"user_name": user_name, "passwd": passwd, "email": email, "nick_name": nick_name, "age": "待完善",
                "sex": "待完善", "phone": "待完善", "message": None}
        users[user_name] = user
        emai = user.get("email")
        email1[emai] = user

        return self.show_login()

    def system_exit(self):
        for i in range(0, 3):
            print("系统将在{}秒后退出".format(3 - i))
            time.sleep(1)
        exit()



    def engine(self):
        self.show_login()





def show_index():
    pass

common = Core




common.engine()









