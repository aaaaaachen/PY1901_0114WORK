import os,sys,time,shelve


# 定义用户对象
class User:
    def __init__(self,username,password,nickname,email):
        self.__username = username
        self.__password = password
        self.__nickname = nickname
        self.__gender = "待完善"
        self.__age = 0
        self.__email = email
        self.__phone = "待完善"
        self.__is_active = True
        self.__remark = "待完善"

    def set_username(self,username):
        self.__username = username

    def get_username(self):
        return self.__username

    def set_password(self,password):
        self.__password = password

    def get_password(self):
        return self.__password

    def set_nickname(self,nickname):
        self.__nickname = nickname

    def get_nickname(self):
        return self.__nickname

    def set_gender(self,gender):
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_age(self,age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_email(self,email):
        self.__email = email

    def get_email(self):
        return self.__email

    def set_phone(self,phone):
        self.__phone = phone

    def get_phone(self):
        return self.__phone

    def set_is_active(self,is_active):
        self.__is_active = is_active

    def get_is_active(self):
        return self.__is_active

    def set_remark(self,remark):
        self.__remark = remark

    def get_remark(self):
        return self.__remark

    # 修改用户密码
    def user_change_password(self):
        password = input("请输入旧密码：")
        if password == self.__password:
            new_password = input("请输入新的密码：")
            c_new_password = input("请再次输入密码：")
            if new_password == c_new_password:
                self.__password = new_password
                print("密码修改成功....")
                print(self.__password)
                core.save_data()
                return "ok"
        else:
            return "error"

    # 完善个人信息
    def user_prefect_information(self):
        print("昵称：",self.__nickname)
        print("性别：",self.__gender)
        print("年龄：",self.__age)
        print("邮箱：",self.__email)
        print("电话：",self.__phone)
        print("备注：",self.__remark)
        res = input("请输入要完善的选项（R键返回）：")
        if res == "昵称":
            nickname = input("请输入昵称：")
            self.__nickname = nickname
            return "ok"
        elif res == "性别":
            gender = input("请输入性别：")
            self.__gender = gender
            return "ok"
        elif res == "年龄":
            age = input("请输入年龄：")
            self.__age = age
            return "ok"
        elif res == "邮箱":
            email = input("请输入邮箱：")
            self.__email = email
            return "ok"
        elif res == "电话":
            phone = input("请输入电话：")
            self.__phone = phone
            return "ok"
        elif res == "备注":
            remark = input("请输入备注：")
            self.__remark = remark
            return "ok"
        elif res.upper() == "R":
            return "error"


# 定义系统对象
class Core:

    def __init__(self):
        self.users = dict()
        self.essays = dict()
        self.online = None

    # 注册方法
    def register(self):
        username = input("请输入账号：")
        if username in self.users:
            print("账号已存在，请重新输入")
            return self.register()
        password = input("请输入密码：")
        c_password = input("请再次输入密码：")
        nickname = input("请输入昵称：")
        email = input("请输入邮箱：")
        if password == c_password:
            print("注册成功.....")
            user = User(username,password,nickname,email)
            # email1 = User(username,password,nickname,email)
            self.users[username] = user
            self.users[email] = user
            core.save_data()
            time.sleep(1)
            return "ok"
        else:
            return "error"

    # 账号密码登录
    def pw_login(self):
        username = input("请输入账号：")
        password = input("请输入密码：")
        if username in self.users and password == self.users.get(username).get_password():
            print("登陆成功")
            self.online = self.users[username]
            time.sleep(1)
            return "ok"
        else:
            res = input("账号或密码错误，请重新输入(R键返回)")
            if res.upper() == "R":
                return "error"
            return self.pw_login()

    # 邮箱密码登录
    def email_login(self):
        email = input("请输入邮箱：")
        password = input("请输入密码：")
        if email in self.users and password == self.users.get(email).get_password():
            print("登陆成功")
            self.online = self.users[email]
            time.sleep(1)
            return "ok"
        else:
            res = input("邮箱或密码错误，请重新输入(R键返回)")
            if res.upper() == "R":
                return "error"
            return self.email_login()

    # 存储数据
    def save_data(self):

        file = shelve.open('data/blog.dat')
        file['users'] = self.users
        file['essays'] = self.essays

    # 获取数据
    def get_data(self):
        file = shelve.open('data/blog.dat')
        self.users = file['users']
        self.essays = file['essays']

    # 退出方法
    def logout(self):
        for i in range(0, 3):
            print("系统将在{}秒后退出".format(3 - i))
            # save_data()
            time.sleep(1)
        exit()


# 登录页面展示
def show_login_display():
    print("############################")
    print("     欢迎来到用户登录中心")
    print("       1.用户登录")
    print("       2.用户注册")
    print("       3.系统退出")
    print("############################")
    choice = input("请输入选项：")
    return show_login_menu.get(choice)() if choice in show_login_menu else show_login_display()


# 登录模块
def show_login():
    print("************************")
    print("      1.账户密码登录")
    print("      2.邮箱密码登录")
    print("************************")
    choice = input("请输入选项：")
    if choice == "1":
        res = core.pw_login()
        if res == "ok":
            # 登录成功，展示首页
            return show_index()
    elif choice == "2":
        res = core.email_login()
        if res == "ok":
            # 登录成功，展示首页
            return show_index()
    else:
        return show_login()


# 注册模块
def show_register():
    res = core.register()
    if res == "ok":
        # 注册成功，展示登录界面
        return show_login_display()


# 退出模块
def show_logout():

    res = core.logout()
    # 退出系统
    exit()


# 展示主页信息
def show_index():
    print("****************************")
    print("          欢迎{}光临".format(core.online.get_username()))
    print("****************************")
    print("          1.个人中心")
    print("          2.文章中心")
    print("          3.信息中心")
    print("          4.返回上一级")
    print("          5.退出系统")
    print("****************************")

    choice = input("请输入选项：")
    return show_index_menu.get(choice)() if choice in show_index_menu else show_index()


# 个人中心展示
def show_personal_center():
    print("##########################")
    print("       1.修改密码")
    print("       2.信息维护")
    print("       3.返回上一级")
    print("##########################")
    choice = input("请输入选项：")
    if choice == "1":
        return change_password()
    elif choice == '2':
        return prefect_inforamtion()
    elif choice == "3":
        return show_index()
    else:
        return show_personal_center()


# 文章中心展示
def show_essay_center():
    pass


# 消息中心展示
def show_message_center():
    pass


# 修改密码界面
def change_password():
    res = core.online.user_change_password()
    if res == "ok":
        core.save_data()
        print("密码修改成功....")
        return show_login_display()
    else:
        return change_password()


# 完善信息界面
def prefect_inforamtion():
    res = core.online.user_prefect_information()
    if res == "ok":
        print("修改成功....")
    return show_personal_center()


core = Core()


# 登录界面字典
show_login_menu = {
    "1":show_login,
    "2":show_register,
    "3":show_logout
}
# 首页界面字典
show_index_menu = {
    "1":show_personal_center,
    "2":show_essay_center,
    "3":show_message_center,
    "4":show_login_display,
    "5":show_logout

}


def engine():
    if not os.path.exists('E:/PY1901_0114WORK/days14/data/blog.dat.dat'):
        core.save_data()
    core.get_data()
    show_login_display()


engine()