'''

'''

import random

cards = []

while True:
    print("********************************")
    print("              1.註冊")
    print("              2.登錄")
    print("              3.退出")
    print("********************************")
    choice = input("請輸入選項")

    if choice == "1":

        while True:
            new_card = {}
            new_name = input("請輸入新的用戶名")
            is_ok = True
            for find_name in cards:

                if new_name == find_name["name"]:
                    print("用戶名已存在，請重新輸入")
                    is_ok = False
            if is_ok == False:
                print(type(is_ok))
                print(is_ok)
                continue

            if new_name == "":
                is_ok = False
                continue
            elif new_name == "r":
                is_ok =False
                break
            new_passwd = input("請輸入新的密碼")

            if new_passwd == "":
                print("密碼不能為空，請重新輸入")
                is_ok = False
                break

            new_addr = input("請輸入地址")

            if new_addr == "":
                print("地址不能為空，請重新輸入")
                is_ok = False
                break

            new_card ={"name":new_name,"passwd":new_passwd,"addr":new_addr}
            cards.append(new_card)
            print(cards)
            input("**********************")
            if is_ok:
                break
            else:
                continue


    elif choice == "2":
        pass
    elif choice == "3":
        pass
    else:
        print("沒有此選項")
        continue