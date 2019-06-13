
import time
import random

bag = [["西红柿",1],\
        ["番茄",2]
]

store = []
user = ["wu","123",100]
users = [
    ["wu","123",0],
    ["wz","123",0]
]

num = 3
sum = 0

while True:
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("\n")
    shop = [
        {"id": 1, "good_name": "西紅柿", "good_price": 10},
        {"id": 2, "good_name": "番茄\t", "good_price": 12},
        {"id": 3, "good_name": "土豆\t", "good_price": 15},
        {"id": 4, "good_name": "黄瓜\t", "good_price": 17},
        {"id": 5, "good_name": "青椒\t", "good_price": 14},
    ]

    for good in shop:
        print("编号:%s 商品  %s 价格  %s" % (good["id"], good["good_name"], good["good_price"]))

    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

    choice = int(input("请输入购买编号："))

    if choice > len(shop) - 1:

        print("无商品")

    else:
        for id in shop:
            if choice == id["id"]:
                print(id["good_name"])
                a = id["good_price"]
        num = int(input("请输入要购买的数量："))
        sum = a * num
        if user[2] < sum:
            print("您的金币不足")
            time.sleep(1)
            break
        else:
            balance = user[2] - sum
            user[2] -= sum
            # good = arr[choice][1]
            # article = [good, num]
            # store.append(article)

            print("     您本次购买的商品是:", good["good_name"])
            print("     您本次消费金币为： ", sum, )
            print("     您的金币还有:\t", balance)
            key = input("     继续购买请按N，退出请按L\n\t\t")
            if key == "N":
                sum = 0
                continue
            elif key == "L":
                break
