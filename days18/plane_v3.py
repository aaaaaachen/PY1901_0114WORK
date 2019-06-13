"""
全民大战飞机
"""

import pygame, random
bullets_allowed = 0
SCREEN_SIZE = (512,768)
SCREEN_RECT =pygame.Rect(0,0,*SCREEN_SIZE)

class GameSprite(pygame.sprite.Sprite):
    def __init__(self,image_path,speed=1,x=0,y=0):
        super().__init__()
        # 初始化数据
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    # 更新方法
    def update(self):
        self.event()
        self.move()

    def event(self):
        """事件操作"""
        bullet_index = 0
        event_list = pygame.event.get()
        if len(event_list) > 0:
            for event in event_list:
                if event.type == pygame.QUIT:
                    # 游戏退出
                    pygame.quit()
                    exit()
                if event.type == ENEMY_EVENT_CREAT:
                    # 创建敌方飞机

                    enemy = EnemySprite("./images/enemy/a1_1.png", random.randint(3, 6))
                    group_enemy.add(enemy)


                    #     group_enemy.add(enemy)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        hero.fire1()

                if event.type == HERO_EVENT_FIRE:
                    hero.fire()


                # if event.type == ENEMY_EVENT_BOOM:
                #     pygame.sprite.groupcollide(group_enemy, hero.group_hero_bullet, True, True)
                #     enemy.boom()






    def move(self):
        self.rect.y += self.speed

class BackgroundSprite(GameSprite):


    def move(self):
        super().move()
        # 边界判断
        if self.rect.y > screen_rect.height:
            self.rect.y = -screen_rect.height

class HeroSprite(GameSprite):
    def __init__(self, image_path, speed, x, y):
        super(HeroSprite, self).__init__(image_path, speed, x, y)

        # 子弹精灵组
        self.group_hero_bullet = pygame.sprite.Group()


    def update(self):
        self.move()
        self.event()

    def move(self):
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > screen_rect.width - self.rect.width:
            self.rect.x = screen_rect.width - self.rect.width
        elif self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > screen_rect.height - self.rect.height:
            self.rect.y = screen_rect.height - self.rect.height

    def event(self):
        key_down = pygame.key.get_pressed()
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.K_SPACE:
                print("fire....")
                self.fire()
        if key_down[pygame.K_UP]:
            print("飞机向上.....")
            self.rect.y -= self.speed
        if key_down[pygame.K_DOWN]:
            print("飞机向下.....")
            self.rect.y += self.speed
        if key_down[pygame.K_LEFT]:
            print("飞机向左.....")
            self.rect.x -= self.speed
        if key_down[pygame.K_RIGHT]:
            print("飞机向右.....")
            self.rect.x += self.speed
        # if key_down[pygame.K_SPACE]:
        #     print("飞机发射子弹...")
        #     self.fire()



    def fire(self):

        bullet = BulletSprite("./images/bullet/bullet_4.png",6,self.rect.x+45,self.rect.y-20)
        self.group_hero_bullet.add(bullet)

    def fire1(self):
        for i in (0,1,2):
            bullet = BulletSprite("./images/bullet/bullet_2.png", 6, self.rect.x + 45, self.rect.y - 20)
            self.group_hero_bullet.add(bullet)

class BulletSprite(GameSprite):

    def move(self):
        self.rect.y -= self.speed

        if self.rect.y < 0:
            self.kill()

class EnemySprite(GameSprite):
    def __init__(self,image_path,speed):
        super().__init__(image_path,speed)


        self.group_enemy_bullet = pygame.sprite.Group()

        self.rect.x = random.randint(0,screen_rect.width - self.rect.width)
        self.rect.y = -self.rect.height

    def move(self):

       self.rect.y += self.speed

       if self.rect.y > screen_rect.height:
            self.kill()
       if self.rect.x >screen_rect.width:
            self.rect.x = -self.speed


    def fire(self):
        bullet1 = BulletSprite("./images/bullet/bullet_3.png", 6, self.rect.x + 45, self.rect.y - 20)
        self.group_enemy_bullet.add(bullet1)

    def boom(self):
        img = pygame.image.load("./images/boom.gif")
        self.screen.blit(img, (self.rect.x, self.rect.y))
        pygame.time.wait(10)
        pygame.display.update()




# 游戏初始化
pygame.init()
res = random.randint(1,3)

# 添加一个飞机创建事件
ENEMY_EVENT_CREAT = pygame.USEREVENT
# 添加一个计时器，触发创建事件
pygame.time.set_timer(ENEMY_EVENT_CREAT,random.randint(500,1000))

# 英雄飞机发射子弹
HERO_EVENT_FIRE = pygame.USEREVENT+1
pygame.time.set_timer(HERO_EVENT_FIRE,random.randint(200,200))

# 添加一个敌方飞机发射子弹事件
ENEMY_EVENT_BOOM = pygame.USEREVENT+1


# 场景初始化
screen_rect = pygame.Rect(0,0,*SCREEN_SIZE)
screen = pygame.display.set_mode((screen_rect.width,screen_rect.height),0,32)

# 创建背景精灵对象
bg1 = BackgroundSprite("./images/maps/img_bg_level_1.jpg")
bg2 = BackgroundSprite("./images/maps/img_bg_level_1.jpg")
bg2.rect.y = -screen_rect.height

# 创建英雄飞机
hero = HeroSprite("images/hero/hero_3.png",speed=5, x=screen_rect.centerx-50,y=screen_rect.centery+300)

# 初始化资源的精灵组
group_init_resource = pygame.sprite.Group(bg1, bg2,hero)

# 创建地方飞机的精灵组
group_enemy = pygame.sprite.Group()

# 初始化子弹精灵组
group_hero_bullet = pygame.sprite.Group()

# 初始化敌方子弹精灵组
group_enemy_bullet = pygame.sprite.Group()

# 刷新频率控制
clock = pygame.time.Clock()
bullet_index = 0
sorce = 0
while True:
    # 刷新频率
    clock.tick(60)
    bullet_index +=1


    # 更新资源精灵组
    group_init_resource.update()
    group_init_resource.draw(screen)

    # 更新子弹精灵组
    hero.group_hero_bullet.update()
    hero.group_hero_bullet.draw(screen)


    # 刷新敌方飞机精灵组
    group_enemy.update()
    group_enemy.draw(screen)

    pygame.sprite.groupcollide(group_enemy, hero.group_hero_bullet, True, True)

    # 英雄飞机精灵 和 敌人飞机精灵组 碰撞检测
    if pygame.sprite.spritecollide(hero, group_enemy,True):
        sorce += 1
        if sorce > 3:
            hero.kill()
            pygame.quit()
    # pygame.sprite.spritecollide(group_enemy,hero,True)

    pygame.display.update()

