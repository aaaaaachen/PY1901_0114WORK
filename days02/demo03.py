'''
围棋棋盘上的芝麻的重量
每个格子中的芝麻的数量是前一个格子的两倍
第一个格子放一粒芝麻，一粒芝麻重0.006kg

'''
print("~~~***~~~***~~~***~~~***~~~***~~~***~~~")
print("      请输入一粒芝麻的重量：")
print("      请输入一共多少个格子：")
print("      请输入第一个格子有多少个芝麻：")
print("~~~***~~~***~~~***~~~***~~~***~~~***~~~")
print("      \n\n\n\n")
a=float(input("\t一个芝麻的重量："))
b=float(input("\t格子的个数:"))
c=float(input("\t第一个格子中芝麻的数量："))
sum=c*(1-2**b)/(1-2)
sum=int(sum)
weight=sum*a/1000
print("   \n\n       重量为",weight)
print(sum)