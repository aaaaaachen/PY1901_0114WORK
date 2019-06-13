'''

'''


# def bankrupt(name,good):
#     print("江南皮革厂倒闭了")
#     print("王八蛋",name,".....")
#     print("带着",good)
#     print("跑了")
#
#
# bankrupt("黄鹤","小姨子")



# def bankrupt(name,good="小姨子"):
#     print("江南皮革厂倒闭了")
#     print("王八蛋",name,".....")
#     print("带着",good)
#     print("跑了")
#
#
# bankrupt("黄鹤")


# def bankrupt(name,*good):
#     print("江南皮革厂倒闭了")
#     print("王八蛋",name,".....")
#     print("带着",good)
#     print("跑了")
#
#
# bankrupt("黄鹤","小姨子","二奶")


# def bankrupt(name,**good):
#     print("江南皮革厂倒闭了")
#     print("王八蛋",name,".....")
#     print("带着",good)
#     print("跑了")
#
#
# bankrupt("黄鹤",girl1="xiaoyizi",girl2="二姨太")


# def bankrupt(*name,**good):
#     print("江南皮革厂倒闭了")
#     print("王八蛋",name,".....")
#     print("带着",good)
#     print("跑了")
#
#
# bankrupt("黄鹤","刘庆东",girl1="小姨子",girl2="二奶")


def bankrupt(name,*,girl1,girl2):
    print("江南皮革厂倒闭了")
    print("王八蛋",name,".....")
    print("带着",girl1,girl2)

    print("跑了")


bankrupt("黄鹤",girl1="小姨子",girl2="二奶")




