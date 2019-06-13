import marshal
a = "dashuaibi"
b = 22
c = 12.3434
d =[1,2,3]
e = {"username":"achen"}
f = False
x = [a,b,c,d,e,f]
# with open('./data/marshal.dat','wb') as file:
#     marshal.dump(len(x),file)
#     for i in x:
#         marshal.dump(i,file)


with open('./data/marshal.dat','rb') as file:
    n = marshal.load(file)

    for x in range(n):
        print(marshal.load(file))