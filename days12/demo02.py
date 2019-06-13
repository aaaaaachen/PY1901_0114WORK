import pygame, sys
import pygame.freetype

#将计算值归一化，0-255
def RGBChannel(a):
    return 0 if a<0 else (255 if a>255 else int(a))

#初始化
pygame.init()

#窗口属性设置
size = width, height = 600, 400
speed =[1,1]
bgcolor = pygame.Color("black")

#设置屏幕可伸缩
screen = pygame.display.set_mode(size, pygame.RESIZABLE)

#设置icon图标和标题
icon = pygame.image.load("datou.jpg")
pygame.display.set_icon(icon)
pygame.display.set_caption("pygame小球和文字运动")

#文字设置
GOLD = 255,251,0
RED = pygame.Color("red")
pos = [230,160]
f1 = pygame.freetype.Font("C://Windows//Fonts//msyh.ttc",36)
f1rect = f1.render_to(screen,pos,"世界和平",fgcolor=GOLD,size = 50)

f1surf, f2rect = f1.render("宇宙和谐",fgcolor=RED,size = 50)
#每秒100次帧刷新，视频中每次展示的静态图像为帧
fps = 100
clock =pygame.time.Clock()

#图像载入
ball = pygame.image.load("datou.jpg")

#返回一个覆盖图像的矩形Rect对象
ballrect = ball.get_rect()

still = False#鼠标按下检测符号

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        #键盘敲击事件
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0])-1)*int(speed[0]/abs(speed[0]))
            elif event.key == pygame.K_RIGHT:
                speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0] - 1
            elif event.key == pygame.K_UP:
                speed[1] =speed[1] + 1 if speed[1] > 0 else speed[1] - 1
            elif event.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[0] == 0 else (abs(speed[0])-1)*int(speed[0]/abs(speed[0]))


        elif event.type == pygame.VIDEORESIZE:
            size = width, height = event.w,event.h
            screen = pygame.display.set_mode(size,pygame.RESIZABLE)

        #鼠标可以通过左键摆放壁球，当释放按键时壁球运动
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                still =True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                still = False
                ballrect = ballrect.move(event.pos[0] - ballrect.left,event.pos[1] - ballrect.top)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button[0] == 1:
                ballrect = ballrect.move(event.pos[0] - ballrect.left,event.pos[1] - ballrect.top)

    #当游戏界面在系统中显示时返回True，否则返回False
    if pygame.display.get_active() and not still:
        #小球运动，矩形移动一个偏移量（x,y）
        ballrect =ballrect.move(speed)



#壁球反弹运动
#遇到左右两侧，横向速度去反；
#遇到上下两侧，纵向速度去反。

    if ballrect.left < 0 or ballrect.right > width:
        speed[0] =- speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] =- speed[1]


        #根据壁球移动的状态修改游戏背景色
        #R:水平距离/窗体宽度
    bgcolor.r = RGBChannel(ballrect.left*255 / width)
    #G垂直距离/窗体高度
    bgcolor.g = RGBChannel(ballrect.top*255 / height)
    #B最小速度/最大速度
    bgcolor.b = RGBChannel(min(speed[0],speed[1])*255 / max(speed[0],speed[1],1))
    screen.fill(bgcolor)

    #文字的移动控制
    if pos[1] < 0 or pos[1] +f1rect.height > height:
        speed[1] =- speed[1]
    if pos[0] < 0 or pos[0] + f1rect.width > width:
        speed[0] =- speed[0]
    pos[0] = pos[0] + speed[0]
    pos[1] = pos[1] + speed[1]

    #将一个图像绘制在另一个图像上，即将src绘制到dect位置上
    #通过Rect对象引入壁球的绘制
    screen.blit(ball,ballrect)

    #绘制文字，方式1
    f1surf,f2rect = f1.render("宇宙和谐",fgcolor= RED,size = 30)
    screen.blit(f1surf,(pos[0]+50,pos[1]+50))

    #绘制文字，方式2
    frect = f1.render_to(screen,pos,"世界和平",fgcolor = GOLD,size = 30)

    #刷新屏幕
    pygame.display.update()

    #控制帧速度，即窗口刷新速度
    clock.tick(fps)

