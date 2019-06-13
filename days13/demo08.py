class userLogReg:
    """
    Created on 2018.11
    @author: tox33
    """

    def __init__(self):
        """
            :param userFile: 操作的文件
        """
        self.userFile = "user.txt"

    def userLogin(self, username, password):
        """
            用户登录
            :param username:用户名
            :param paaword:密码
            :return:True，用户登录成功；False，用户登录失败
        """
        try:
            f = open(self.userFile, "r", encoding="utf-8")
            for line in f:
                line = line.strip()
                line_list = line.split("#")
                if line_list[0] == username and line_list[1] == password:
                    return True
                elif line_list[0] == username and line_list[1] != password:
                    print("密码错误！！")
            return False
        except IOError:
            return False

    def userRegister(self, username, password):
        """
            用户注册
            1、打开文件
            2、用户名#密码
            :param username:用户名
            :param password:密码
            :return:True，注册成功
        """
        with open(self.userFile, "a", encoding="utf-8")as f:
            temp = "\n" + username + "#" + password
            f.write(temp)
            return True

    def user_exist(self, username):
        """
            检测用户名是否存在
            :param username:要检测的用户名
            :return: True，用户名存在；False，用户名不存在
        """
        try:
            with open(self.userFile, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    line_new = line.split("#")
                    if line_new[0] == username:
                        return True
                return False
        except IOError:
            return False

    def main(self):
        """
            主控制函数
            :操作选择参数arg: 0-注册 1-登录
        """
        print("欢迎来到Al用户管理系统")
        while (True):
            arg = input("0：注册 ，1：登录\n")
            if arg == "0":
                user = input("请设置用户名：")
                if self.user_exist(user):
                    print("用户名已存在，请重新设置！")
                    continue
                else:
                    pwd = input("请设置密码：")
                    if self.userRegister(user, pwd):
                        print("注册成功！")
                        continue
                    else:
                        print("注册失败！")
                        continue
            elif arg == "1":
                user = input("请输入用户名：")
                if not self.user_exist(user):
                    print("用户名不存在，请检查！")
                    continue
                else:
                    pwd = input("请输入登录密码：")
                    if self.userLogin(user, pwd):
                        print("登录成功！")
                        break
                    else:
                        print("登录失败，请检查！")
                        continue
            else:
                print("输入错误，请检查！")
                continue


if __name__ == '__main__':
    test = userLogReg()
    test.main()
