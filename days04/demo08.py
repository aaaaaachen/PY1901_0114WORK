i=0
while True:
    file = open('C:/username.txt', 'a+')
    file.seek(0)
    users = []
    for line in file:
        username = line.strip()
        users.append(username)
    username = input('请输入用户名：')
    passwd = input('请输入密码：')
    c_passwd = input('请再次输入密码：')

    if username == '' or passwd == '' or c_passwd == '':
        print("用户名或者密码不能为空或再次确认密码不能为空")
    elif c_passwd != passwd :
        i+=1
        print('密码和确认密码不一致')
        if i==3:
            break
    elif username in users:
            print('用户名已经存在')
    else:
        print('恭喜你，注册成功！')
        print("请登录")
        a = input("请输入用户名")
        b = input("请输入密码")
        file.write(username+'\n')
        file.close()
        user = [a,b]
        if user in users:
            print("登陆成功")
        # file.write(username+'\n')
        # file.close()
        # break


    print("请登录")
    a = input("请输入用户名")
    b = input("请输入密码")
    user = [a,b]
    if user in users:
        print("登陆成功")