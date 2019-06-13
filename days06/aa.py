# # arr = [
# #         ["编号","商品\t","价格"],\
# #         [1,"西红柿",12],\
# #         [2,"番茄\t",15],\
# #         [3,"蛋炒饭\t",20],\
# #         [4,"红烧排骨",50],\
# #         [5,"被子\t",90],\
# #         [6,"帐篷\t",120]
# # ]
# # # for i  in  range(len(arr)):
# # #     for j in range(len(arr[0])):
# # #         print(arr[i][j],end="\t\t\t")
# # #     print("\r\n")
# # a = arr[1][1]
# # b = arr[1][2]

# # arr1 = [a,b]

# # # print(arr[1][1],arr[1][2])
# # # arr11=["西红柿",12]
# # for i in range(len(arr1)):
# #     print(arr1[i],end="\t")
# # # print(arr1)
# # # print(a)


# # a = [["w",1],["e",2]]
# # b = [["w",1],["e",2]]
# # a.extend(b)
# # print(a)

import random
bag = [["西红柿",1],["番茄",2]]
while True:
        # a=input("请输入：")
        # for i in range(len(bag)):
        #         if  bag[i][0]==a:
        #                 print(i)
        #                 break
        # b = bag[i][1]
        # print(bag[i][0],b)
        a = input("请输入背包的食物：")
        for i in range(len(bag)):
                if bag[i][0] == a:
                        print(i)
                        break
                else:
                        input("输入有误，请重新输入")
                        continue
        print(bag[i][1],"还有",bag[i][0],"个")
        b = int(input("输入放入的数量："))
        if b > bag[i][1]:
                input("背包中数量不足,请重新输入：\n")
                break
        else:
                bag[i][1] -= b
                print("背包中还有",bag[i][1])
                c = input("继续购买请按c,返回请按l:\n")
                if c == "c":
                        continue
                elif c == "l":
                        break
                else:
                        print("输入有误，请重新输入：")
 
     
         


# import os,sys,time,random
# store = [["西红柿",1],["番茄",2]]
# bag=[]

# while True:
#         os.system("cls")
#         for i in range(len(store)):
#                 for j in range(len(store[0])):
#                         print(store[i][j],end = "\t")
#                 print("\r\n")
#         print("##########################################")
#         print("          1.往背包中添加东西")
#         print("          2.返回上一界面")
#         print("##########################################")
#         choice = input("请输入选项：")

#         if choice == "1":

#                 a = input("请输入要添加的东西：")
#                 for i in range(len(store)):
#                         if store[i][0] == a:
#                                 print(i)
#                         break
#         # else:
#         #     print("输入有误，请重新输入：")
#         #     a = input("")
#         #     if a == "r":
#         #         time.sleep(1)
#         #         break
#         #     else:
#         #         time.sleep(1)
#         #         continue
#         print(store[i][0],"还有",store[i][1],"个")
#         b = int(input("请输入要添加的数量："))
#         if b > store[i][1]:
#                 print("商品不足，请重新输入")
#                 continue
#         else:
#                 store [i][1] -= b
#                 goods = [a,b]
#                 bag.append(goods)
#                 print(store[i][0],"还有",store[i][1],"个")
#                 c = input("继续添加请按c,返回请按l:\n")
#                 if c == "c":
#                         continue
#                 elif c == "l":
#                         break
#                 else:
#                         print("输入有误，请重新输入：")
#                         continue
#                 break

#         if choice == "2":
#                 print("即将返回上一级")
#                 time.sleep(1)
#                 break
#         else:
#                 a = input("没有此选项，请重新输入(按r键返回)\n")
#                 if a == "r":
#                         time.sleep(1)
#                         break
#                 else:
#                         time.sleep(1)
#                         continue

