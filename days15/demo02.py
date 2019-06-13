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


# 定义管理员对象
class Manager:
    def __init__(self, account, password,is_active):

        self.__is_active = True
        self.__account = account
        self.__password = password

    def set_account(self, account):
        self.__account = account

    def get_account(self):
        return self.__account

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password

    def set_is_active(self, is_active):
        self.__is_active = is_active

    def get_is_active(self):
        return self.__is_active

    def add_user(self):
        pass

    def cancel_user(self):
        pass

    def lock_user(self):
        pass

    def unlock_user(self):
        pass

    def find_user(self):
        pass


#定义超级管理员对象
class Controller(Manager):
    def __init__(self,account,password,is_active):
        super().__init__(account,password)

    def __add_manager(self):
        pass

    def __cancel_manager(self):
        pass

    def set_lock_mamager(self,lock_manager):
        self.__lock_manager = lock_manager

    def get_lock_manager(self):
        return self.__lock_manager()

    def __unlock_manageer(self):
        pass

    def __find_manager(self):
        pass


# 定义系统对象
class Core(User,Manager):

    def __init__(self):
        self.accounts = dict()
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
        username = input("请输入账号|邮箱：")
        password = input("请输入密码：")
        if username in self.users and password == self.users.get(username).get_password() and self.users.get(username).get_is_active() == True:
            print("登陆成功")
            self.online = self.users[username]
            time.sleep(1)
            return "ok"
        elif username in self.users and password == self.users.get(username).get_password() and self.users.get(username).get_is_active() == False:
            print("账号已被封锁")
            time.sleep(1)
            return "error"
        else:
            res = input("账号或密码错误，请重新输入(R键返回)")
            if res.upper() == "R":
                return "error"
            return self.pw_login()



    # 管理员登录
    def manager_login(self):
        account = input("请输入账号：")
        password = input("请输入密码：")
        if account == "wu" and password == "123":
            return "supermanager"
        elif account in self.accounts and password == self.accounts.get(account).get_password() and self.accounts.get(account).get_is_active() == True:
            print("登陆成功....")
            return "manager"
        elif account in self.accounts and password == self.accounts.get(account).get_password() and self.accounts.get(account).get_is_active() == False:
            print("账号已被封锁.....")
            time.sleep(1)
            return "error"
        else:
            res = input("输入账号或密码错误,按任意键继续...（按R键返回）")
            if res.upper() == "R":
                return show_login_display()
            else:
                return self.manager_login()

    # 增加管理员账号
    def add_manager(self):
        account = input("请输入账号：")
        if account in self.accounts:
            print("账号已存在，请重新输入：")
            return "false"
        password = input("请输入密码：")
        c_password = input("请再次输入密码：")
        if password == c_password:
            is_active = True
            print("增加成功....")
            new_account = Manager(account,password,is_active)
            self.accounts[account] = new_account
            return "ok"
        else:
            res = input("两次密码不一致，请重新输入(R键返回)：")
            if res.upper() == "R":
                return "R"
            else:
                self.add_manager()
    # 锁定管理员
    def lock_manager(self):
        core.find_manager()
        res = input("请输入要操作的账号：")
        if res in core.accounts:
            if core.accounts.get(res).get_is_active() == True:
                choice = input("是否锁定 {}  Y/N".format(res))
                if choice.upper() == "Y":
                    core.accounts.get(res).set_is_active(False)
                    return "ok"
                elif choice.upper() =="N":
                    return "false"
            elif core.accounts.get(res).get_is_active() == False:
                choice = input("是否解锁 {}  Y/N".format(res))
                if choice.upper() == "Y":
                    core.accounts.get(res).set_is_active(True)
                    return "ok"
                elif choice.upper() == "N":
                    return "false"
        else:
            return self.lock_manager()

    # 锁定用户
    def lock_user(self):
        core.find_user()
        res = input("请输入要操作的账号：")
        if res in core.users:
            if core.users.get(res).get_is_active() == True:
                choice = input("是否锁定 {}  Y/N".format(res))
                if choice.upper() == "Y":
                    core.users.get(res).set_is_active(False)
                    return "ok"
                elif choice.upper() =="N":
                    return "false"
            elif core.users.get(res).get_is_active() == False:
                choice = input("是否解锁 {}  Y/N".format(res))
                if choice.upper() == "Y":
                    core.users.get(res).set_is_active(True)
                    return "ok"
                elif choice.upper() == "N":
                    return "false"
        else:
            return self.lock_user()


    # 删除管理员
    def clean_manager(self):
        print("aaaaa")
        core.find_manager()
        print("aaaaa")
        choice = input("请输入要删除的账号(R键返回)：")
        if choice in core.accounts:
            core.accounts.pop(choice)
            return "ok"
        elif choice.upper() == "R":
            return "back"
        else:
            return "error"

    # 删除用户
    def clean_user(self):
        core.find_user()
        choice = input("请输入要删除的账号(R键返回)：")
        if choice in core.users:
            core.users.pop(choice)
            return "ok"
        elif choice.upper() == "R":
            return "back"
        else:
            return "error"



    # 查看管理员
    def find_manager(self):
        for account in core.accounts:
            print("账号：{}  激活状态：{}".format(core.accounts.get(account).get_account(),core.accounts.get(account).get_is_active()))

    # 查看用户
    def find_user(self):
        for user in core.users:
            print("账号：{}  激活状态：{}".format(core.users.get(user).get_username(),core.users.get(user).get_is_active()))

    # 存储数据
    def save_data(self):

        file = shelve.open('data/demo02.dat')
        file['users'] = self.users
        file['essays'] = self.essays

    # 获取数据
    def get_data(self):
        file = shelve.open('data/demo02.dat')
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
    print("       4.管理员登录")
    print("############################")
    choice = input("请输入选项：")
    return show_login_menu.get(choice)() if choice in show_login_menu else show_login_display()


# 登录模块
def show_login():

    res = core.pw_login()
    if res == "ok":
        # 登录成功，展示首页
        return show_index()
    elif res == "error":
        return show_login_display()
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


def show_manager_login():
   res = core.manager_login()
   if res == "supermanager":
       return show_manager_index()
   elif res == "manager":
       return manage_user_index()
   else:
       return show_manager_login()


# 展示增加管理员
def show_add_manager():
    res = core.add_manager()
    if res == "ok":
        return manage_manager_index()
    elif res == "R":
        return show_manager_index()
    else:
        return show_add_manager()

# 展示增加用户
def show_add_user():
    res = core.register()
    if res == "ok":
        # 注册成功，展示登录界面
        return manage_user_index()



# 展示锁定管理员
def show_lock_manager():
    res = core.lock_manager()
    if res == "ok":
        print("操作成功....")

        return manage_manager_index()
    elif res == "false":
        print("未执行操作")
        return manage_manager_index()
    else:
        return show_lock_manager()

# 展示锁定用户
def show_lock_user():
    res = core.lock_user()
    if res == "ok":
        print("操作成功....")

        return manage_user_index()
    elif res == "false":
        print("未执行操作")
        return manage_user_index()
    else:
        return show_lock_user()

# 展示删除管理员
def show_clean_manager():
    res = core.clean_manager()
    if res == "ok":
        print("操作成功....")
        time.sleep(1)
        return manage_manager_index()
    elif res == "back":
        return manage_manager_index()
    else:
        print("操作失败")
        return show_clean_manager()

# 展示删除用户
def show_clean_user():
    res = core.clean_user()
    if res == "ok":
        print("操作成功....")
        time.sleep(1)
        return manage_user_index()
    elif res == "back":
        return manage_user_index()
    else:
        print("操作失败")
        return show_clean_user()





# 管理员首页
def show_manager_index():
    print("*****************************")
    print("            1.管理管理员")
    print("            2.管理用户")
    print("            3.返回首页")
    print("*****************************")
    choice = input("请输入选项：")
    return show_manager_index_dict.get(choice)() if choice in show_manager_index_dict else show_manager_index()


# 管理管理员首页
def manage_manager_index():
    print("########################")
    print("     1.增加管理员")
    print("     2.锁定|解锁管理员")
    print("     3.删除管理员")
    print("     4.查看管理员")
    print("     5.返回上一级")
    print("########################")
    choice = input("请输入选项：")
    return manage_manager_index_dict.get(choice)() if choice in manage_manager_index_dict else manage_manager_index()

#管理用户首页
def manage_user_index():
    print("########################")
    print("     1.增加用户")
    print("     2.锁定|解锁用户")
    print("     3.删除用户")
    print("     4.查看用户")
    print("     5.返回上一级")
    print("########################")
    choice = input("请输入选项：")
    return manage_user_index_dict.get(choice)() if choice in manage_user_index_dict else manage_user_index()

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
    "3":show_logout,
    "4":show_manager_login
}
# 首页界面字典
show_index_menu = {
    "1":show_personal_center,
    "2":show_essay_center,
    "3":show_message_center,
    "4":show_login_display,
    "5":show_logout

}

#管理员登录界面字典
show_manager_index_dict = {
    "1":manage_manager_index,
    "2":manage_user_index,
    "3":show_login_display
}
# 管理管理员界面字典
manage_manager_index_dict = {
    "1":show_add_manager,
    "2":show_lock_manager,
    "3":show_clean_manager,
    "4":core.find_manager,
    "5":show_login_display
}
# 管理用户界面字典
manage_user_index_dict = {
    "1":show_add_user,
    "2":show_lock_user,
    "3":show_clean_user,
    "4":core.find_user,
    "5":show_login_display
}




def engine():
    if not os.path.exists('E:/PY1901_0114WORK/days15/data/demo02.dat.dat'):
        core.save_data()
    core.get_data()
    show_login_display()


engine()