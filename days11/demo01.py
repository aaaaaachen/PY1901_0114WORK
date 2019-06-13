# '''
# 将程序中的数据写入到文件中
# '''
# file = open('./w.text','w',encoding='utf-8')
# message = "dashuaibi"
# file.write(message)
# file.close()


# file  = open(file='./w.text',mode='r',encoding='utf-8')
# text = file.read()
# print(text)
# file.close()

# file = open(file ='C:/Users/Administrator/Desktop/83fdef15-d605-4892-aadb-b1f7a0357ea6.png',mode='rb')
# photo = file.read()
# print(photo)


# with open('C:/Users/Administrator/Desktop/83fdef15-d605-4892-aadb-b1f7a0357ea6.png','rb') as file1:
# #     with open('./'+file1.name[file1.name.rfind('/'):],'wb') as file2:
# #         file2.write(file1.read())


# with open('Z:/share/Python人工智能1901/第一阶段/days11/随堂视频/PY基础_0380_文件IO概述.mp4','rb') as file1:
#     with open('C:/Users/Administrator/Desktop/视频/'+file1.name[file1.name.rfind('/'):],'wb') as file2:
#         file2.write(file1.read())

with open('Z:/share/Python人工智能1901/第一阶段/days11/随堂视频/PY基础_0410_with语句及字符串切片.mp4','rb') as file1:
    with open('C:/Users/Administrator/Desktop/视频/'+file1.name[file1.name.rfind('/'):],'wb') as file2:
        file2.write(file1.read())