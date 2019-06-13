'''
个人博客开发项目
author：阿辰
'''

import time, random

users = {}
online = None
essays = {}
recyclebin = {}
comment = {}
message1 = {}
email1 ={}
accont = {}

#登录界面展示
def show_login():
    print("*******************************")
    print("          1.登录")
    print("          2.注册")
    print("          3.退出")
    print("*******************************")

    choice = input("请输入选项：")
    return show_login_menu.get(choice)() if choice in show_login_menu else show_login()




#注册界面
def show_register():
    print("********************")
    print("欢迎来到注册中心")
    print("********************")
    register()


#退出系统
def system_exit():
    for i in range(0,3):
        print("系统将在{}秒后退出".format(3-i))
        time.sleep(1)
    exit()

# 首页展示
def show_index():
    print("****************************")
    print("          1.个人中心")
    print("          2.文章中心")
    print("          3.信息中心")
    print("          4.返回上一级")
    print("          5.退出系统")
    print("****************************")

    choice = input("请输入选项：")
    return show_index_menu.get(choice)() if choice in show_index_menu else show_index()


# 个人中心
def personal_center():
    print("****************************")
    print("         1.修改密码")
    print("         2.完善个人资料")
    print("         3.返回首页")
    print("****************************")

    choice = input("请输入选项：")
    return personal_center_menu.get(choice)() if choice in personal_center_menu else personal_center()

# 修改密码
def update_passwd():
    passwd = input("请输入您的密码（R键返回）：")
    if passwd.upper() == "R":
        return show_index()
    if passwd != online.get("passwd"):
        print("输入密码有误，请重新输入")
        return update_passwd()
    else:
        new_passwd = input("请输入新的密码")
        if new_passwd == passwd:
            print("新密码和老密码相同，请重新输入：")
            return update_passwd()
        c_new_passwd = input("请再次输入密码：")
        if new_passwd != c_new_passwd:
            print("两次输入密码不一致，请重新输入：")
            time.sleep(1)
            return update_passwd()
        else:
            online["passwd"] = new_passwd
            print("修改成功")
            return show_login()


#完善个人信息
def prefect_self_info():
    for i in online.keys():
        print(i,"\t\t",online.get(i))
    re = input("请输入要修改的名称：")
    if re in online.keys():
        print(online[re])
        matter = input("请输入要修改的内容")
        online[re] = matter
        print("修改成功")
        return personal_center()
    else:
        return prefect_self_info()


#文章中心
def essay_center():
    print("************************************")
    print("          1.发表文章")
    print("          2.查看所有文章")
    print("          3.查看个人文章")
    print("          4.管理个人文章")
    print("          5.返回首页")
    print("************************************")

    choice = input("请输入选项：")
    return essay_center_menu.get(choice)() if choice in essay_center_menu else essay_center()


#发表文章
def essay_publish():
    title = input("      请输入文章题目：")
    if title in essays:
        print("文章题目已被占用，请重新命题：")
        return essay_publish()
    content = input("     请输入文章内容：")
    essay = {"title":title,"content":content,"author":online,"read_count":0}
    essays[title] = essay
    print("     文章正在发表中.....")
    time.sleep(1)
    print("     发表成功....")
    return essay_center()

#文章详情
def essay_detail(title,is_ok):
    essay = essays.get(title)
    rc = essay.get("read_count")
    rc += 1
    essay["read_count"] = rc
    print("文章标题:{}".format(essay.get("title")))
    print("文章作者：{}".format(essay.get("author").get("user_name")))
    print("阅读次数：{}".format(essay.get("read_count")))
    print("文章内容：{}".format(essay.get("content")))
    print("文章评论：{}".format(comment.items()))
    if is_ok:
        re = input("是否要添加评论Y/N")
        if re.upper() == "Y":
            if essay.get("author").get("user_name") != online["user_name"]:
                comm = input("请输入您的评论：")
                comment[online["user_name"]] = comm
                time.sleep(1)
                print("评论成功")
                return essay_center()
            else:
                print("自己的文章不能评论")
                return look_essays()
        elif re.upper() == "N":
            return essay_center()
        else:
            return essay_detail(title,is_ok)




#查看所有文章
def look_essays():
    print("标题\t\t作者")
    for title in essays.keys():
        print(title,essays[title]["author"].get("user_name"))
    title = input("请输入要看的文章：（按R键返回首页）")
    if title.upper() == "R":
        return show_index()
    else:
        if title in essays:
            is_ok = True
            essay_detail(title,is_ok)
        else:
            print("没有这篇文章")
            return look_essays()


#查看自己的文章
def look_self_essay():
    print("标题\t\t作者")
    for title in essays.keys():
        if essays[title]["author"].get("user_name") == online["user_name"]:
            print(title, essays[title]["author"].get("user_name"))
    title = input("请输入要看的文章：（按R键返回首页）")
    if title.upper() == "R":
        return show_index()
    else:
        if title in essays:
            is_ok = False
            essay_detail(title,is_ok)
        else:
            print("没有这篇文章")
            return look_self_essay()


#管理个人文章
def regulate_self_essay():
    print("################################")
    print("         1.修改文章")
    print("         2.删除文章")
    print("         3.回收站")
    print("         4.返回上一级")
    print("################################")

    choice = input("请输入选项：")
    return regulate_self_essay_menu.get(choice)() if choice in regulate_self_essay_menu else regulate_self_essay()

#修改个人文章
def update_self_essay():
    for title in essays.keys():
        if essays[title]["author"].get("user_name") == online["user_name"]:
            print("标题\t\t作者")
            print(title, essays[title]["author"].get("user_name"))
    re = input("请输入要修改文章的标题：")
    if re in essays:
        print(essays.get(re).get("content"))
        content = input("请输入修改内容：")
        essays.get(re)["content"] = content
        return regulate_self_essay()
    else:
        return update_self_essay()

#删除个人文章
def delate_self_essay():
    for title in essays.keys():
        if essays[title]["author"].get("user_name") == online["user_name"]:
            print("标题\t\t作者")
            print(title, essays[title]["author"].get("user_name"))
    dela = input("请输入要删除的文章：")
    if dela in essays:
        recyclebin[dela] = essays.pop(dela)
        print("删除成功")
        print(recyclebin)
        return regulate_self_essay()

#回收站
def recycle_bin():
    print("***************************")
    print("      1.恢复文档")
    print("      2.永久删除文档")
    print("      3.返回上一级")
    print("***************************")

    choice = input("请输入选项：")
    return recycle_bin_menu.get(choice)() if choice in recycle_bin_menu else recycle_bin()

#恢复文档
def recover_essay():
    print("标题\t\t作者")
    for essay in recyclebin.keys():
        print(essay,recyclebin[essay]["author"]["user_name"])
    re = input("请输入要恢复的文章：")
    if re in recyclebin.keys():
        essays[re] = recyclebin[re]
        recyclebin.pop(re)
        print("恢复成功")
        return essay_center()

# 永久删除文档
def dela_essay_forever():
    print("标题\t\t作者")
    for essay in recyclebin.keys():
        print(essay, recyclebin[essay]["author"]["user_name"])
    re = input("请输入要销毁的文章：")
    if re in recyclebin.keys():
        dela = input("是否确定要销毁")
        if dela == "是":
            recyclebin.pop(re)
            print("销毁成功")
            return essay_center()
        elif dela == "否":
            return recycle_bin()
        else:
            return dela_essay_forever()


# 信息中心
def message_center():
    print("**************************")
    print("      1.收到的信息")
    print("      2.发送消息")
    print("      3.返回上一级")
    print("**************************")

    choice = input("请输入选项：")
    if choice == "1":
        recive_message()
    elif choice == "2":
        send_message()
    elif choice == "3":
        show_index()
    else:
        return message_center()


# 发送信息
def send_message():
    for i in users.keys():
        print("用户：{}".format(i))
    choice_user = input("请输入要发信息的对象：")
    if choice_user in users.keys():
        print("您发送信息的对象是：{}".format(choice_user))
        message = input("请输入要发送的信息：")
        message1[online.get("user_name")] = message
        users[choice_user]["message"] = message1
        print("发送中.....")
        time.sleep(1)
        print("对方已接收....")
        return message_center()
    else:
        print("您输入的对象不存在")
        return message_center()


# 收到的信息
def recive_message():
    message1 = online.get("message").keys()
    if message1 is not None:
        print(online.get("message").keys())
        choice = input("请输入要谁的信息：")
        if choice in online.get("message"):

            print(online.get("message").get(choice))
            input("按任意键返回")
            return message_center()
        else:
            print("没有收到消息")
            return message_center()

#注册函数
def register():
    user_name = input("请输入账号:")
    if user_name in users:
        print("账号已经存在，请重新注册")
        return register()
    passwd = input("请输入密码:")
    c_passwd = input("请再次输入密码")
    email = input("请输入邮箱：")
    nick_name = input("请输入昵称")
    if passwd != c_passwd:
        print("两次输入密码不一致，请重新输入：")
        return register()
    print("注册成功")
    user = {"user_name":user_name,"passwd":passwd,"email":email,"nick_name":nick_name,"age":"待完善","sex":"待完善","phone":"待完善","message":None}
    users[user_name] = user
    emai = user.get("email")
    email1[emai] = user

    return show_login()


#登录函数
def loading():
    print("****************************")
    print("       1.账号密码登录")
    print("       2.邮箱密码登录")
    print("****************************")

    choice = input("请输入选项(R键返回)：")
    #重新定义全局变量
    global online
    if choice.upper() == "R":
        return show_login()
    #账号密码登录
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
            return loading()
    #邮箱密码登录
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
            return loading()
    else:
        return loading()
# 登录引擎函数
def engine():
    show_login()



show_login_menu = {
    "1":loading,
    "2":show_register,
    "3":system_exit
}

show_index_menu = {
    "1":personal_center,
    "2":essay_center,
    "3":message_center,
    "4":show_login,
    "5":system_exit
}

personal_center_menu = {
    "1":update_passwd,
    "2":prefect_self_info,
    "3":show_index
}

essay_center_menu = {
    "1":essay_publish,
    "2":look_essays,
    "3":look_self_essay,
    "4":regulate_self_essay,
    "5":show_index
}

regulate_self_essay_menu = {
    "1":update_self_essay,
    "2":delate_self_essay,
    "3":recycle_bin,
    "4":essay_center
}

recycle_bin_menu = {
    "1":recover_essay,
    "2":dela_essay_forever,
    "3":regulate_self_essay
}

engine()
