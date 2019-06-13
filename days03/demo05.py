import random
import os

range1=int(input("请输入本局游戏的最小值："))
range2=int(input("请输入本局游戏的最大值："))
num=random.randint(range1,range2)

guess="guess"
n=0

while guess!=num:
    n+=1
    guess=int(input("请输入你猜的数字："))
    if guess<num:
        print("您猜的数小了...")
        
    elif guess>num:       
        print("您猜的数大了...")
        
else:
    print("恭喜您猜对了")
    print("您一共猜了",n,"次哦！")
    if n==1:
        integral=10
    elif n==2:
        integral=8
    elif n==3:
        integral=6
    elif n==4:
        integral=4
    elif n==5:
        integral=2
    else:
        integral=0
    print("您的积分为：",integral,"分")
    



