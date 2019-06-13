import os,sys,time

users = [
    ['admin', '123'],
    ['manager', '123']
]

while True:
    os.system("cls")
    print("111111111111111111111111111111111111111111")
    print("            1.用户登录")
    print("            2.用户注册")
    print("            3.退出系统")
    print("            4.修改信息")
    print("111111111111111111111111111111111111111111")

    choice = input("请输入选项：")

    if choice == "1":
        while True:
            is_ok=True
            username = input("请输入姓名")

            if username=="R":
                is_ok=False
                break
            passwd = input("请输入密码")

            if passwd=="R":
                is_ok=False 
                break

            for user in users:
                if username==user[0] and passwd==user[1]:
                    # 登陆成功
                    print("登陆成功")
                    is_ok = True
                    break
                else:
                    print("账号或密码有误")
                continue
            
            if is_ok:
                break
            else:
                continue
        
        while True:
            print("#######################")
            print("    欢迎",username,"光临")
            print("\t1.购物超市")
            print("\t2.休闲游戏")
            print("\t3.返回登录")
            print("\t4.退出系统")
            print("########################")
            
            break



        time.sleep(1)
        break



    

    elif choice == "2":
        pass
    elif choice =="3":
        print("33333333333")
    else:
        print("没有此选项")
        continue
