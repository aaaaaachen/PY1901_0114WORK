import random

username=input("请输入用户名：")
passwd=input("请输入注册密码：")

user=[]
user.append(username)
user.append(passwd)

users=[]
users.append(user)
print("success")

username = input("请输入登录名：")
passwd = input("密码：")

for user in users:

    if user[0]==username and user[1]==passwd:
        input("登录成功")
        break
    else:
        print("输入账户或密码有误")
