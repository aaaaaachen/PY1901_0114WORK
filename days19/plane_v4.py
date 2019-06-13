"""
飞机大战V4
"""

import pygame, random, sys

SCREEN_SIZE = (512,768)
SCREEN_RECT = pygame.Rect(0, 0, *SCREEN_SIZE)

class GameSprite(pygame.sprite.Sprite):
    def __init__(self,image_path,speed=1,x=0,y=0):
        super().__init__()
        # 初始化数据
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def move(self):
        self.rect.y -= self.speed

class BackgroundSprite(GameSprite):
    def __init__(self,image_path,next = False):
        super().__init__(image_path)
        if next:
            self.rect.y = -SCREEN_SIZE[1]

    def move(self):
        super().move()

        if self.rect.y > SCREEN_SIZE[1]:
            self.rect.y = SCREEN_SIZE[1]

class HeroSprite(GameSprite):
    def __init__(self, image_path, speed, x, y):
        super(HeroSprite, self).__init__(image_path, speed, x, y)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.y = SCREEN_RECT.centery + 300

        # 子弹精灵组
        self.group_hero_bullet = pygame.sprite.Group()

    def update(self):
        self.move()


    def move(self):
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > SCREEN_SIZE[0] - self.rect.width:
            self.rect.x = SCREEN_SIZE[0] - self.rect.width
        elif self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > SCREEN_SIZE[1] - self.rect.height:
            self.rect.y = SCREEN_SIZE[1] - self.rect.height



    def fire(self):
        if len(self.group_hero_bullet) < 10:
            # 创建子弹
            bullet = BulletSprite("./images/bullet/bullet_3.png",6,self.rect.x+45,self.rect.y-20)
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

        self.rect.x = random.randint(0,SCREEN_SIZE[0] - self.rect.width)
        self.rect.y = -self.rect.height

    def move(self):
        self.rect.y += self.speed
        self.fire()

        if self.rect.y > e.screen_rect.height:
            self.kill()

    def fire(self):
        bullet = BulletSprite("./images/bullet/bullet_3.png", 6, self.rect.x + 45, self.rect.y - 20)
        self.group_enemy_bullet.add(bullet)

class Engine:
    def __init__(self):
        self.screen_rect = pygame.Rect(0,0,*SCREEN_SIZE)
        self.screen = pygame.display.set_mode((self.screen_rect.width,self.screen_rect.height),0,32)
        self.create_scnce()



    def create_scnce(self):
        bg1 = BackgroundSprite("./images/maps/img_bg_level_1.jpg",next = False)
        bg2 = BackgroundSprite("./images/maps/img_bg_level_1.jpg",next = True)



        self.group_enemy = pygame.sprite.Group()
        self.group_hero_bullet = pygame.sprite.Group()
        self.group_enemy_bullet = pygame.sprite.Group()
        self.hero = HeroSprite("images/hero/hero_3.png", speed=5, x=self.screen_rect.centerx - 50,
                               y=self.screen_rect.centery + 300)
        self.group_init_resource = pygame.sprite.Group(bg1, bg2, self.hero)

        self.ENEMY_CREATE = pygame.USEREVENT

    def update_sence(self):
        # 更新资源精灵组
        self.group_init_resource.update()
        self.group_init_resource.draw(self.screen)

        # 更新子弹精灵组
        self.hero.group_hero_bullet.update()
        self.hero.group_hero_bullet.draw(self.screen)

        # 刷新敌方飞机精灵组
        self.group_enemy.update()
        self.group_enemy.draw(self.screen)

        pygame.display.update()

    def game_start(self):
        pygame.init()
        pygame.time.set_timer(self.ENEMY_CREATE, 2000)

        clock = pygame.time.Clock()
        while True:
            clock.tick(30)
            self.create_scnce()
            self.update_sence()
            self.check_collide()
            self.check_event()
            pygame.display.update()




    def check_event(self):
        '''事件监听'''
        # 监听所有事件
        event_list = pygame.event.get()
        if len(event_list) > 0:
            print(event_list)
            for event in event_list:
                print(event.type, pygame.KEYDOWN, pygame.K_LEFT)
                # 如果当前的事件：是quit事件
                if event.type == pygame.QUIT:
                    # 卸载所有pygame,退出程序
                    pygame.quit()
                    exit()
                if event.type == self.ENEMY_CREATE:
                    enemy = EnemySprite("./images/enemy/a1_1.png", random.randint(3, 6))
                    # 添加敌方飞机精灵组
                    self.group_enemy.add(enemy)
        key_down = pygame.key.get_pressed()
        if key_down[pygame.K_UP]:
            print("飞机向上.....")
            self.hero.rect.y -= 5
        elif key_down[pygame.K_DOWN]:
            print("飞机向下.....")
            self.hero.rect.y += 5
        elif key_down[pygame.K_LEFT]:
            print("飞机向左.....")
            self.hero.rect.x -= 5
        elif key_down[pygame.K_RIGHT]:
            print("飞机向右.....")
            self.hero.rect.x += 5
        elif key_down[pygame.K_SPACE]:
            print("飞机发射子弹...")
            self.hero.fire()

    def check_collide(self):
        pygame.sprite.groupcollide(self.group_enemy, self.hero.group_hero_bullet, True, True)

        # 英雄飞机精灵 和 敌人飞机精灵组 碰撞检测
        sorce = 0
        if pygame.sprite.spritecollide(self.hero, self.group_enemy, True):
            sorce += 1
            if sorce > 3:
                self.hero.kill()
                pygame.quit()
        # pygame.sprite.spritecollide(group_enemy,hero,True)


    def __game_login(self):
        pass
        # 游戏开始界面

    def __game_step(self):
        pass
        # 游戏关卡

    def __game_quit(self):
        pass


e = Engine()
e.game_start()