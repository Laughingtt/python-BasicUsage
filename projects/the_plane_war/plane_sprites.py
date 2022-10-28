import random
import pygame

# 定义屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 定义刷新帧率的常量
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):

        # 调用父类的初始化方法
        super().__init__()

        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):

        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""
    def __init__(self, is_alt=False):

        # 1.调用父类方法实现精灵的创建
        super().__init__("./images/background.png")

        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):

        # 1.调用父类的方法实现
        super().update()

        # 2.判断是否移出屏幕，如果移出，将图像移至屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):

        # 1.调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__("./images/enemy1.png")
        # 2.指定敌机的初始随机速度——1到3
        self.speed = random.randint(1, 3)

        # 3.指定敌机的初始随机位置
        self.rect.bottom = 0   # 设置敌机是从屏幕外飞进屏幕
        # 敌机要完整的在屏幕内 — 敌机的最大X值是屏幕的宽减去敌机的宽
        max_x = SCREEN_RECT.width-self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):

        # 1.调用父类方法保持垂直方向的飞行
        super().update()
        # 2.判断是否飞出屏幕，如果是 需要从精灵组中删除敌机
        if self.rect.y >= SCREEN_RECT.height:    # 敌机的y值大于屏幕的高即飞出屏幕
            # print("飞出屏幕，需从精灵组中删除...")
            # kill方法可以将精灵从所有精灵组中移出，精灵就好被自动销毁
            self.kill()

    # 判断敌机是否被销毁
    def __del__(self):
        # print("敌机挂了 %s" % self.rect)
        pass


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):

        # 1.调用父类方法设置image和速度
        super().__init__("./images/me1.png", 0)
        # 2.设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 3.创建子弹的精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):

        # # 英雄在水平方向移动
        # self.rect.x += self.speed

        # 控制英雄不能离开屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.width:
            self.rect.right = SCREEN_RECT.width
        elif self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.bottom > SCREEN_RECT.bottom:
            self.rect.bottom = SCREEN_RECT.bottom

    def fire(self):

        # 1.创建子弹精灵
        # bullet = Bullet()
        # bullet1 = Bullet()
        # bullet2 =Bullet()

        # # 2.设置子弹精灵的位置
        # bullet.rect.bottom = self.rect.y - 20
        # bullet1.rect.bottom = self.rect.y
        # bullet2.rect.bottom = self.rect.y -40
        # bullet.rect.centerx = self.rect.centerx
        # bullet1.rect.centerx = self.rect.centerx
        # bullet2.rect.centerx = self.rect.centerx

        for i in (0, 1, 2):

            # 1.创建子弹精灵
            bullet = Bullet()

            # 2.设置子弹的位置
            bullet.rect.bottom = self.rect.y - i*20
            bullet.rect.centerx = self.rect.centerx

            # 3.将精灵添加到精灵组
            self.bullets.add(bullet)
        pass


class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):

        # 调用父类方法设置子弹图片和初始速度
        super().__init__("./images/bullet2.png", -10)

    def update(self):

        # 调用方法让子弹沿垂直方向飞行
        super().update()

        # 判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

    # def __del__(self):
    #     print("子弹被销毁")