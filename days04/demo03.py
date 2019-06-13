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
