'''
#个人博客项目开发
author:阿辰
'''

import time, random

users = {}
online = None

articles = {}
user = {"user_name":"wu","passwd":"123","hobby":"basketball","sex":"female","fanifesto":"大帅比"}
users = {"wu":user}


#注册功能
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



#展示登录菜单
def show_login():
    print("*****************************")
    print("1.用户登录")
    print("2.用户注册")
    print("3.退出系统")
    print("*****************************")
    choice = input("请输入选项：")

    return show_login_menu.get(choice)() if choice in show_login_menu else show_login()

#展示首页菜单
def show_index():
    print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")
    print("\t\t1. 查看所有文章")
    print("\t\t2. 查看个人文章")
    print("\t\t3. 发表文章")
    print("\t\t4. 个人信息维护")
    print("\t\t5. 返回上一级")
    print("\t\t6. 退出系统")
    print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")
    choice = input("请输入选项：")

    return show_index_menu.get(choice)() if choice in show_index_menu else show_index()

#展示登录界面
def show_register():
    register()
    return show_login()

#登录函数
def loading():
    user_name = input("请输入账号(r键返回)：")
    if user_name.upper() == "R":
        return show_login()
    passwd = input("请输入密码(r键返回)：")
    if passwd.upper() == "R":
        return show_login()
    if user_name in users and passwd == users[user_name]["passwd"]:
        global online
        online = users.get(user_name)
        print("登录成功")
        return show_index()
    else:
        print("账户或密码错误，请重新输入")

        return loading()



def system_exit():
    for i in range(0,3):
        print("系统将在{}秒后退出".format(3-i))
        time.sleep(1)
    exit()


def perfect_self_info():
    print("aihao:{}".format(online["hobby"]))
    hobby = input("请输入爱好")
    online["hobby"] = hobby

    return self_update()


def update_passwd():
    passwd = input("请输入您的密码（R键返回）：")
    if passwd.upper()== "R":
        return show_index()
    if passwd != online.get("passwd"):
        print("输入密码有误，请重新输入")
        return update_passwd()
    else:
        new_passwd = input("请输入新的密码")
        c_new_passwd = input("请再次输入密码：")
        if new_passwd != c_new_passwd:
            print("两次输入密码不一致，请重新输入：")
            time.sleep(1)
            return update_passwd()
        else:
            online["passwd"] = new_passwd
            print("修改成功")
            return show_login()



def  self_update():
    print("**************************")
    print("\t\t1.修改密码")
    print("\t\t2.修改个人信息")
    print("\t\t3.返回首页")
    print("**************************")
    choice = input("请输入选项：")

    return show_self_update.get(choice)() if choice in show_self_update else show_index()


def look_articles():
    print("标题\t\t作者")
    for title_key in articles.keys():
        print(title_key,"\t\t",articles.get(title_key).get("author").get("user_name"))

    title = input("请输入要看的文章：（按R键返回首页）")
    if title.upper() == "R":
        return show_index()
    else:
        if title in articles:
            article_detail(title)
        else:
            print("没有这篇文章")
            return look_articles()

def look_self_articles():
    print("标题\t\t作者")
    for title_key in articles.keys():

        if articles.get(title_key).get("author").get("user_name") == online.get("user_name"):
            print(title_key,"\t\t",articles.get(title_key).get("author").get("user_name"))
    title = input("请输入要查看的文章（按R键返回首页）")
    if title.upper() == "R":
        return show_index()
    if title in articles:
        article_detail(title)
    else:
        print("没有这篇文章")
        return look_self_articles()

def article_detail(title):
    article = articles.get(title)
    rc = article.get("read_count")
    rc += 1
    article["read_count"] = rc
    print("文章标题:{}".format(article.get("title")))
    print("文章作者：{}".format(article.get("author").get("user_name")))
    print("阅读次数：{}".format(article.get("read_count")))
    print("文章内容：{}".format(article.get("content")))

    input("按任意键返回")
    return show_index()


def article_publish():
    title = input("文章标题：")
    if title in articles:
        print("文章名已被占用，请使用其他标题")
        time.sleep(1)
        return article_publish()
    content = input("请输入文章内容：")

    article = {"title":title,"content":content,"author":online,"read_count":0}
    articles[title] = article
    print("文章发表中....")
    time.sleep(1)
    print("文章发表成功")
    return show_index()



def engine():
    show_login()





show_login_menu = {
    "1":loading,
    "2":show_register,
    "3":system_exit
    }

show_index_menu = {
    "1": look_articles,
    "2": look_self_articles,
    "3": article_publish,
    "4": self_update,
    "5": show_login,
    "6": system_exit
}

show_self_update = {
    "1":update_passwd,
    "2":perfect_self_info,
    "3":system_exit
}



engine()