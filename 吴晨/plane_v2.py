# -*- coding: utf-8 -*-
'''
飞机大战
    面向对象全民飞机大战
'''
# 导入pygame,random,time模块
import pygame, random, time
pygame.mixer.init()
# 定义屏幕尺寸大小
SCREEN_SIZE =(512,768)
# 定义屏幕位置参数
SCREEN_RECT =pygame.Rect(0,0,*SCREEN_SIZE)
# EVENT_HERO_FIRE = pygame.USEREVENT
# 定义事件
ENEMY_CREATE = pygame.USEREVENT+1
ENEMY1_CREATE = pygame.USEREVENT+2
ENEMY_CREATE_BULLET = pygame.USEREVENT+3
SKILL_CREATE = pygame.USEREVENT+4
AUTO_FIRE = pygame.USEREVENT+5
# bullet_index = 0
screen = pygame.display.set_mode(SCREEN_SIZE)

# 定义游戏类 继承pygame.sprite.Sprite类
class GameSprite(pygame.sprite.Sprite):

    # 定义GameSprite属性
    def __init__(self,image_path,speed=1):

        super().__init__()

        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.speed = speed
    # 定义更新方法
    def update(self):
        self.move()
    # 定义移动方法
    def move(self):
        self.rect.y += self.speed

# 定义背景类，继承GameSprite
class BackgroundSprite(GameSprite):
    # 定义背景属性
    def __init__(self, image_path, speed,prepare = False):
        super().__init__(image_path, speed=1)
        self.speed = speed

        if prepare:
            self.rect.y = -SCREEN_SIZE[1]
    # 定义更新方法
    def update(self):
        super().update()

        if self.rect.y > SCREEN_SIZE[1]:
            self.rect.y = -SCREEN_SIZE[1]
# 定义英雄飞机类 继承GameSprite
class HeroSprite(GameSprite):

    # 定义英雄飞机属性
    def __init__(self,image_path,speed):
        super().__init__(image_path,speed)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.y = SCREEN_RECT.centery+300
        self.group_hero_bullet = pygame.sprite.Group()
        self.group_hero_bullet_R = pygame.sprite.Group()
        self.bullet_img = bullet_list[1]
        self.is_ok = True
        self.bullet_width = [65,10,55,3,20]

    # 定义英雄飞机更新方法
    def update(self):
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > SCREEN_RECT.width -self.rect.width:
            self.rect.x = SCREEN_RECT.width -self.rect.width
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > SCREEN_RECT.height - self.rect.height:
            self.rect.y = SCREEN_RECT.height - self.rect.height
        self.move()
        self.fire()

    #定义英雄飞机移动方法
    def move(self):
        key_down = pygame.key.get_pressed()
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

    # 定义英雄开火的方法
    def fire(self):
        if len(self.group_hero_bullet) <= 0:
            bullet = BulletSprite(self.bullet_img,speed=8,x=self.rect.x - 10 ,y=self.rect.y - 20)
            bullet1 = BulletRightSprite(self.bullet_img,speed=8,x=self.rect.x - 10 ,y=self.rect.y - 20)
            bullet2 = BulletLeftSprite(self.bullet_img,speed=8,x=self.rect.x - 10 ,y=self.rect.y - 20)
            if self.is_ok:
                self.group_hero_bullet.add(bullet)
            else:
                self.group_hero_bullet.add(bullet,bullet1,bullet2)

    # 定义英雄开火的方法
    def fire1(self):
        bullet = BulletRightSprite(bullet_list[e.step],speed=8,x=self.rect.centerx-self.bullet_width[e.step-1], y=self.rect.centery-40)
        bullet1 = BulletLeftSprite(bullet_list[e.step],speed=8,x=self.rect.centerx-self.bullet_width[e.step-1], y=self.rect.centery-40)
        self.group_hero_bullet.add(bullet,bullet1)
        fire_music = pygame.mixer.Sound("./music/sheji.wav")
        fire_music.play()

    # 定义英雄开火的方法
    def fire3(self):

        bullet = BulletSprite(bullet_list[10], speed=8, x=self.rect.x - 200, y=self.rect.y - 20)
        self.group_hero_bullet_R.add(bullet)
        # fire_music = pygame.mixer.Sound("./music/sheji.wav")
        # fire_music.play()

# 定义子弹类型
class BulletSprite(GameSprite):
    # 定义子弹属性
    def __init__(self,image_path,speed,x,y):
        super().__init__(image_path)
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    #定义更新方法
    def update(self):
        self.rect.y -= self.speed
        # 边界判断
        if self.rect.y < 0:
            # kill自己
            self.kill()
    def __del__(self):
        print("子弹销毁")
        # 将子弹移除子弹组
        e.group_enemy_bullet.remove(self)
        print("子弹从子弹组中移除")

# 定义向右边子弹类
class BulletRightSprite(GameSprite):
    # 自身类属性
    def __init__(self,image_path,speed,x,y):
        super().__init__(image_path)
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    # 定义更新方法
    def update(self):
        self.rect.y -= self.speed
        self.rect.x += 2
        # 边界判断
        if self.rect.y < 0:
            self.kill()

    def __del__(self):
        print("子弹销毁")
        e.group_enemy_bullet.remove(self)
        print("子弹从子弹组中移除")


# 定义左子弹类
class BulletLeftSprite(GameSprite):
    # 定义自身属性
    def __init__(self, image_path, speed, x, y):
        super().__init__(image_path)
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    # 定义更新方法
    def update(self):
        self.rect.y -= self.speed
        self.rect.x -= 2
        # 边界判断
        if self.rect.y < 0:
            self.kill()

    def __del__(self):
        print("子弹销毁")
        e.group_enemy_bullet.remove(self)
        print("子弹从子弹组中移除")


# 定义Boss子弹类
class BossBulletSprite(GameSprite):
    # 定义子弹属性
    def __init__(self, image_path, speed, x, y,x_speed):
        super().__init__(image_path)
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.x_speed = x_speed

    # 定义更新方法
    def update(self):
        self.rect.y -= self.speed
        if self.rect.x > SCREEN_RECT.width - self.rect.width:
            self.x_speed = -self.speed

        if self.rect.x < 0:
            self.x_speed = -self.speed

        # 边界判断
        if self.rect.y < 0:
            # kill自己
            self.kill()

    def __del__(self):
        print("子弹销毁")
        # 将子弹移除子弹组
        e.group_enemy_bullet.remove(self)
        print("子弹从子弹组中移除")

# 定义敌机类 继承GameSprite
class EnemySprite(GameSprite):
    def __init__(self,image_path,speed,x_speed,hp=100):
        super().__init__(image_path,speed)
        # 初始化飞机的位置
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)
        self.rect.y = -self.rect.height
        self.x_speed = x_speed
        self.hp = hp
     # 定义移动方法
    def move(self):
        self.rect.y += self.speed
        self.rect.x += self.x_speed
        # x轴边界判断
        if self.rect.x > SCREEN_RECT.width - self.rect.width:
            # 改变自身移动方向
            self.x_speed = -self.x_speed
        # x 轴边界判断
        if self.rect.x <=0:
            # 改变自身运动方向
            self.x_speed = -self.x_speed
    # 定义更新方法
    def update(self):
        self.move()

        # 边界判断
        if self.rect.y > SCREEN_RECT.height:
            # 飞机超出屏幕,自毁
            self.kill()
    # 定义敌机开火
    def fire(self):
        # if len(e.group_enemy_bullet) <= 0:
        bullet = BulletSprite(bullet_list[5],speed=-(self.speed+3),x=self.rect.x+30 ,y=self.rect.y+20)
        # 装填子弹
        e.group_enemy_bullet.add(bullet)

    # 重写__del__魔法方法，产生爆炸效果
    def __del__(self):
        print("敌机销毁")
        # boom_sound = pygame.mixer.Sound("music/boom.wav")
        # boom_sound.play()
        booms = ["images/boom/boom_1.png",
                 "images/boom/boom_2.png",
                 "images/boom/boom_3.png",
                 "images/boom/boom_4.png",
                 "images/boom/boom_5.png",
                 "images/boom/boom_6.png"]
        for i in booms:
            e.screen.blit(pygame.image.load(i), (self.rect.x, self.rect.y))
            # time.sleep(0.005)
            pygame.display.update()
        # 将敌机移除敌机组
        e.enemy_group.remove(self)

# 定义敌机boss类 继承GameSprite
class BossSprite(GameSprite):
    # 定义自身属性
    def __init__(self,image_path,speed,blood=100):
        super().__init__(image_path,speed)
        self.blood = blood
    # 定义自身移动方法
    def move(self):
        self.rect.x += self.speed

        if self.rect.x > SCREEN_RECT.width - self.rect.width:
            self.speed = -self.speed
        if self.rect.x <=0:
            self.speed = -self.speed
    # 重写父类更新方法
    def update(self):
        self.move()
        super().update()

    #重写父类开火方法
    def fire(self):

        bullet = BossBulletSprite(bullet_list[random.randint(7,9)], speed=-7, x=self.rect.centerx, y=self.rect.centery,x_speed=2)
        # bullet.is_ok = True
        e.group_boss_bullet.add(bullet)

    # 定义自身爆炸方法
    def boom(self):

        booms = [
            "images/boss_boom/01.png",
            "images/boss_boom/02.png",
            "images/boss_boom/03.png",
            "images/boss_boom/04.png",
            "images/boss_boom/05.png",
            "images/boss_boom/06.png",
            "images/boss_boom/07.png",

            # "images/boss_boom/011.png",
            # "images/boss_boom/012.png",
            # "images/boss_boom/013.png",
            # "images/boss_boom/014.png",
            # "images/boss_boom/014.png",
            # "images/boss_boom/015.png",
            # "images/boss_boom/016.png",
            # "images/boss_boom/017.png",
            # "images/boss_boom/018.png",
            # "images/boss_boom/019.png",
            # "images/boss_boom/020.png",
            # "images/boss_boom/021.png",
            # "images/boss_boom/022.png"
        ]
        for i in booms:
            e.screen.blit(pygame.image.load(i), (self.rect.x, self.rect.y))
            # time.sleep(0.005)
            pygame.display.update()

# 定义技能包类 继承GameSprite
class Skill_Pack(GameSprite):
    # 自身属性
    def __init__(self,image_path,speed,num):
        super().__init__(image_path,speed)
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)
        self.rect.y = -self.rect.height
        self.num = num

    # 重写父类移动方法
    def move(self):
        self.rect.y += self.speed

        # 边界判断
        if self.rect.y > SCREEN_RECT.height - self.rect.height:
            self.kill()
            # 将自身移除技能组
            e.group_skill_pack.remove(self)
    # 重写父类更新方法
    def update(self):
        super().update()
        # self.skill()
    # def skill(self):
    #     a = random.randint(1,2)
    #     if a == 2:
    #         e.life + 1
    #     elif a == 1:
    #         e.hero.is_ok = False

# 定义启动游戏类
class Engine:
    # 定义启动游戏的属性
    def __init__(self):
        # pygame加载
        pygame.init()
        # 窗口名称
        pygame.display.set_caption("空军一号")
        # 引入字体
        pygame.font.init()
        # 设置字体
        self.game_font = pygame.font.SysFont("fzshuti",30,True)
        # 定义屏幕显示
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        # 定义初始官卡
        self.step = 1
        # 定义英雄生命值
        self.life = 100
        # 定义初始分数
        self.sorce = 0

        self.num = 0
        # 初始化场景
        self.create_sence()
        # 加载背景音效
        pygame.mixer.music.load("music/bgmusic.mp3")
        # 循环播放背景音乐
        pygame.mixer_music.play(-1)
        # 设置关卡临界值
        # self.step_score_list = [20, 80, 120, 200, 300]
        # 定义事件发生时间
        pygame.time.set_timer(ENEMY_CREATE,random.randint(400,800))
        pygame.time.set_timer(ENEMY1_CREATE, random.randint(400,800))
        # pygame.time.set_timer(EVENT_HERO_FIRE,500)
        pygame.time.set_timer(ENEMY_CREATE_BULLET,random.randint(2000,4000))
        pygame.time.set_timer(SKILL_CREATE,random.randint(10000,20000))
        pygame.time.set_timer(AUTO_FIRE, 1000)
        # 定义刷新时钟
        self.clock = pygame.time.Clock()

    def create_sence(self):
        # 初始化背景图片，使其循环播放
        bg1 = BackgroundSprite(maps_list[self.step-1],speed=self.step)
        bg2 = BackgroundSprite(maps_list[self.step-1],speed=self.step, prepare=True)
        # 创建玩家飞机对象
        self.hero = HeroSprite(hero_list[self.step-1], speed=self.step+2)
        # 将背景玩家加入到游戏资源组中
        self.resources = pygame.sprite.Group(bg1, bg2, self.hero)
        # 初始化敌机组
        self.enemy_group = pygame.sprite.Group()
        # 初始化敌机子弹组
        self.group_enemy_bullet = pygame.sprite.Group()
        # 初始化boss组
        self.boss_group = pygame.sprite.Group()
        # 初始化boss子弹组
        self.group_boss_bullet = pygame.sprite.Group()
        # 初始化技能背包组
        self.group_skill_pack = pygame.sprite.Group()

    # 定义更新场景方法
    def update_sence(self):
        # 更新资源组将其渲染到屏幕
        self.resources.update()
        self.resources.draw(self.screen)
        # 更新敌机组将其渲染到屏幕
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        # 更新boss组将其渲染到屏幕
        self.boss_group.update()
        self.boss_group.draw(self.screen)
        # 更新敌机子弹组将其渲染到屏幕
        self.group_enemy_bullet.update()
        self.group_enemy_bullet.draw(self.screen)
        # 更新boss子弹组将其渲染到屏幕
        self.group_boss_bullet.update()
        self.group_boss_bullet.draw(self.screen)
        # 更新英雄飞机子弹组将其渲染到屏幕
        self.hero.group_hero_bullet.update()
        self.hero.group_hero_bullet.draw(self.screen)
        # 更新英雄大招子弹将其渲染到屏幕
        self.hero.group_hero_bullet_R.update()
        self.hero.group_hero_bullet_R.draw(self.screen)
        # 更新技能包组将其渲染到屏幕
        self.group_skill_pack.update()
        self.group_skill_pack.draw(self.screen)
        # 将当前得分和生命值显示到屏幕
        self.screen.blit(self.game_font.render('Score: %s' % self.sorce, True, [222, 211, 0]), [20, 20])
        self.screen.blit(self.game_font.render('hp: %s' % self.life, True, [255, 222, 0]), [20, 50])
        self.screen.blit(self.game_font.render('kill: %s' % self.num, True, [255, 222, 0]), [20, 700])
        # pygame显示更新
        pygame.display.update()

    def level(self):
        bg = pygame.image.load(level_list[self.step-1])
        self.screen.blit(bg, (0, 0))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.start()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()



    # 定义游戏开始方法
    def start(self):
        self.num = 0
        # 清空资源组数据
        self.group_enemy_bullet.empty()
        self.enemy_group.empty()
        self.resources.empty()
        self.group_skill_pack.empty()
        self.hero.group_hero_bullet_R.empty()
        self.hero.group_hero_bullet.empty()
        self.group_boss_bullet.empty()
        # 创建游戏场景
        self.create_sence()
        while True:
            self.clock.tick(80)
            self.check_event()
            self.check_collide()
            self.update_sence()

            # 判断是否升级
            if self.num >20*self.step and len(self.boss_group) <= 0:
                self.sorce +=1
                self.step += 1
                # 当到第五关时，游戏不在升级
                if self.step >5:
                    self.step = 5
                    continue
                return self.level()

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
                # 创建敌机事件
                if event.type == ENEMY_CREATE:
                    self.enemy = EnemySprite(enemy_dict[str(random.randint(1,10))],speed=random.randint(2,3)*self.step,x_speed=random.randint(-5,5))
                    self.enemy_group.add(self.enemy)


                # 敌机创建子弹事件
                if event.type == ENEMY_CREATE_BULLET:
                    # 敌机开火
                    for enemy in self.enemy_group:
                        enemy.fire()
                    # boss 开火
                    if len(self.boss_group)>=0:
                        for boss in self.boss_group:
                            boss.fire()
                # 技能包释放事件
                if event.type == SKILL_CREATE:
                    self.skill = Skill_Pack(skill_pack_list[random.randint(0,1)], speed=1,num=random.randint(1,2))
                    self.group_skill_pack.add(self.skill)
                # 获取键盘点击键盘事件
                if event.type == pygame.KEYDOWN:
                    # 按空格英雄开火1
                    if event.key == pygame.K_SPACE:
                        self.hero.fire1()
                    # R键英雄放大招
                    if event.key == pygame.K_r:
                        # 放大招分数要超过20分，放一次大招减少20分
                        if self.sorce > 20:
                            if len(self.hero.group_hero_bullet_R) <= 0:
                                music = pygame.mixer.Sound("music/boom.wav")
                                music.play()
                                self.hero.fire3()
                                self.sorce -= 20

                        # else:
                        #     self.screen.blit(self.game_font.render('energy shortage', True, [255, 222, 0]), [20, 50])
                        #     time.sleep(0.005)
                        #     pygame.display.update()
    # 定义创建boss方法
    def creat_boss(self):
        if len(self.boss_group)<=0:
            self.boss = BossSprite(boss_list[self.step-1],speed=1)
            self.boss_group.add(self.boss)
    # 定义碰撞碰撞检测方法
    def check_collide(self):
        # 敌机与英雄子弹碰撞
        accident= pygame.sprite.groupcollide(self.enemy_group, self.hero.group_hero_bullet, True, True)
        if len(accident)>0:
            print("sssssssssssssssssssssssssssssssssssssssssssss")
            print(accident)
            print(list(accident.keys()))
            self.sorce += 1
            self.num += 1
            if self.num >= 16*1.25**self.step:
                self.creat_boss()

        # 敌机，敌机子弹，boss子弹 与英雄大招碰撞
        pygame.sprite.groupcollide(self.enemy_group,self.hero.group_hero_bullet_R,True,False)
        pygame.sprite.groupcollide(self.group_enemy_bullet,self.hero.group_hero_bullet_R,True,False)
        pygame.sprite.groupcollide(self.group_boss_bullet,self.hero.group_hero_bullet_R,True,False)
        # boss组与英雄子弹碰撞
        a = pygame.sprite.groupcollide(self.boss_group,self.hero.group_hero_bullet,False,True)
        if a:
            # 每次碰撞boss血量减少5，分数加1
            self.boss.blood -= 5
            self.sorce += 1
            self.num += 1
            # 当boss血量小于等于0，将boss移除boss组
            if self.boss.blood <=0:
                boom_sound = pygame.mixer.Sound("music/death.wav")
                boom_sound.play()
                self.boss.boom()
                boom_sound = pygame.mixer.Sound("music/boom.wav")
                boom_sound.play()
                self.boss_group.remove(self.boss)
                self.step + 1

            else:
                self.boss.boom()
        # 英雄与敌机子弹组，敌机组，boss子弹组，boss组碰撞
        e = pygame.sprite.spritecollide(self.hero,self.group_enemy_bullet,True)
        e1 = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        e2 = pygame.sprite.spritecollide(self.hero,self.group_boss_bullet,True)
        e3 = pygame.sprite.spritecollide(self.hero,self.boss_group,True)
        # 当英雄与敌机子弹组，敌机组，boss子弹组，boss组碰撞时，英雄飞机生命值-1
        if len(e) >0 or len(e1) > 0 or len(e2) >0 or len(e3) > 0:
            self.life -= 1
            self.hero.rect.centerx = SCREEN_RECT.centerx
            self.hero.rect.y = SCREEN_RECT.centery + 300
            if self.life <= 0:
                print("游戏结束")
                pygame.mixer_music.stop()
                self.hero.kill()
                # 返回到GameOver界面
                return self.show_game_over()
        # 英雄与技能组碰撞
        e4 = pygame.sprite.spritecollide(self.hero,self.group_skill_pack,True)
        if e4:
            # 当英雄与技能组碰撞时，升级英雄子弹
            if self.skill.num == 1:
                self.hero.is_ok = False
                self.hero.bullet_img = bullet_list[1]
            elif self.skill.num == 2:
                self.life += 1
            # for skill in self.group_skill_pack:
            #     skill.skill()
    # 定义游戏开始界面
    def show_index(self):
        super().__init__()
        bg = pygame.image.load("images/ui/index.jpg")
        self.screen.blit(bg,(0,0))
        self.screen.blit(pygame.image.load("images/ui/start_menu.png"),(180,590))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 180 <= event.pos[0] <= 300 and 300 <= event.pos[1]:
                        self.level()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
    # 重新开始方法
    def begin(self):
        e.__init__()
        e.start()
    # GameOver界面展示
    def show_game_over(self):
        super().__init__()
        bg = pygame.image.load("images/ui/bg_menu.bmp")
        self.screen.blit(bg, (0, 0))
        self.screen.blit(pygame.image.load("images/ui/restart1.png"), (190, 590))
        self.screen.blit(pygame.image.load("images/ui/Gameover.png"), (5, 200))
        self.screen.blit(self.game_font.render('游戏得分：%s' % self.sorce, True, [255, 0, 0]), [150, 450])
        self.screen.blit(self.game_font.render("继续加油", True, [255, 0, 0]), [180, 500])
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 190 <= event.pos[0] <= 300 and 300 <= event.pos[1]:
                        self.begin()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


# 子弹组
bullet_list = [ "./images/bullet/bullet_1.png",
                "./images/bullet/bullet_2.png",
                "./images/bullet/bullet_3.png",
                "./images/bullet/4.png",
                "./images/bullet/zidan.png",
                "./images/bullet/3.png",
                "./images/bullet/bullet_8.png",
                "./images/bullet/boss_bullet.png",
                "./images/bullet/boss_bullet1.png",
                "./images/bullet/peiqi.png",
                "./images/bullet/bullet_11.png"
                ]


# 敌机组
enemy_dict = {
    "1": "images/enemy/a1_1.png",
    "2": "images/enemy/a1_2.png",
    "3": "images/enemy/a2_1.png",
    "4": "images/enemy/a2_2.png",
    "5": "images/enemy/a3_1.png",
    "6": "images/enemy/a3_2.png",
    "7": "images/enemy/a4_1.png",
    "8": "images/enemy/a4_2.png",
    "9": "images/enemy/diji1.png",
    "10": "images/enemy/diji3.png",
}
#boss子弹组
boss_bullet_list = [
    "images/boss_bullet/boss_bullet.png",
    "images/boss_bullet/boss_bullet1.png"]
# boss组
boss_list = [
    "images/boss/boss_1.png",
    "images/boss/boss_2.png",
    "images/boss/boss_3.png",
    "images/boss/boss_4.png",
    "images/boss/boss_5.png"
]
# 英雄组
hero_list = [
     "images/hero/hero_1.png",
     "images/hero/hero_2.png",
     "images/hero/2.png",
     "images/hero/hero_4.png",
     "images/hero/hero_5.png"]
# 技能包组
skill_pack_list = [
    "images/skill_pack/skill_1.png",
    "images/skill_pack/skill_2.png"
]
# 游戏背景组
maps_list = ["images/maps/img_bg_level_1.jpg",
            "images/maps/img_bg_level_2.jpg",
            "images/maps/img_bg_level_3.jpg",
            "images/maps/img_bg_level_4.jpg",
            "images/maps/img_bg_level_5.jpg"]
# 关卡组
level_list = [
            "images/level/level1.png",
            "images/level/level2.png",
            "images/level/level3.png",
            "images/level/level4.png",
            "images/level/level5.png",
]


e = Engine()
e.show_index()


