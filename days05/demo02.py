

# 创建空列表
a1 = list() #推荐
a2 = []
print(a1,a2)

# 创建非空列表
a1 = list(["ww","qq"])
a2 = ["qq",]

#列表中增加数据
a3 = ["qq","2","fddfd"]

# 末尾增加数据
a3.append("5")

# 
for i in a3:
    print(i)



for i,x in enumerate(a3):
    print("id",i,"source",x)


x = [1,5,2,3,5,6,2,5,7,8,8,4,2,1,5,8,3,10,11]

print(x.count(3))

res=x.pop()

print(res)
print(x)

x.sort()
print(x)

x.reverse()
print(x)

print(max(x),min(x))

print(len(x))


x1=x.copy()
print(x1)

x.clear()
print(x)