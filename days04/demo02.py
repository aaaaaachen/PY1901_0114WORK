# #  ticket 票
# ticket = 10000
# kong_bu_xi_ji = 8888 # 恐袭
# while ticket > 0:
#      # 循环执行的代码
#      print("卖出一张票：", ticket)

#      if kong_bu_xi_ji == ticket:
# #         # 假定遇到了突发事件
#          print("遇到突发事件：有恐怖分子出入，立刻终止业务")
#          break

#      # 改变循环条件
#      ticket -= 1

# print("美好的一天结束了")

# # 3. 循环控制——continue关键字
# i=10
# while i>0:
#     print("nihao")
#     if i==3:
#         print("1111")
#     i-=1
# print("ok")

# i=10
# while i>0:
#     i-=1
#     print("chushouyizhangpiao",i+1)
#     if i==1:
#         print("kuaimaiwanle")
#         continue
    
# print("下班真好")


ticket = 4
is_ok=True
while ticket>0:
    print("正常售票：卖出",ticket,"号票")
    event=(input("是否有突发事件："))
    if event=="是":
        is_ok=False
        print("地震了，快跑")
        break
    ticket-=1

if is_ok:
    print("正常下班")
print("真舒服")
