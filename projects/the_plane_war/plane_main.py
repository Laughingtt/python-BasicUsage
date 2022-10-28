import pygame
from plane_sprites import *


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化")

        # 1.创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2.创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3.调用私有方法，精灵和精灵组的创建
        self.__create_sprites()

        # 4.设置定时器事件——创建敌机 1S
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    # 定义精灵和精灵组
    def __create_sprites(self):
        # 创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)
        # bg2起始位置在bg1的上方
        # bg2.rect.y = -bg2.rect.height

        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄的精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    # 游戏循环
    def start_game(self):
        print("游戏开始...")

        while True:
            # 1.设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 2.事件监听
            self.__even_handler()
            # 3.碰撞检测
            self.__check_collide()
            # 4.更新/绘制精灵组
            self.__update_sprites()
            # 5.更新屏幕显示
            pygame.display.update()

            pass

    # 定义事件监听函数
    def __even_handler(self):
        for event in pygame.event.get():

            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # print("敌机出场...")
                # 创建敌机精灵
                enemy = Enemy()

                # 将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            # 直接判断键盘按键不能持续的获取按键事件
            # elif event.type == pygame.KEYDOWN and event.type == pygame.K_RIGHT:
            #     print("向右移动...")

        # 使用键盘模块提供的方法获取键盘按键——键盘模块可以持续的获取键盘按键
        keys_pressed = pygame.key.get_pressed()
        # 判断元祖中对应的按键索引值
        if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
            self.hero.rect.x += 20
        elif keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
            self.hero.rect.x -= 20
        elif keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
            self.hero.rect.y -= 20
        elif keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
            self.hero.rect.y += 20
        else:
            self.hero.speed = 0

    # 定义碰撞检测
    def __check_collide(self):

        # 1.子弹摧毁敌机—— groupcollide可以判断两个精灵组之间是否碰撞
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)

        # 敌机撞毁英雄——spritecollide可以判断精灵和精灵组之间是否碰撞
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)

        # 判断列表是否有内容
        if len(enemies) > 0:

            # 让英雄牺牲
            self.hero.kill()

            # 结束游戏
            PlaneGame.__game_over()

    # 定义精灵组调用update()和draw()方法实现屏幕更新
    def __update_sprites(self):

        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    # 游戏结束
    @staticmethod
    def __game_over():
        print("游戏结束...")

        pygame.quit()
        exit()


if __name__ == '__main__':

    # 创建游戏对象
    game = PlaneGame()

    # 启动游戏
    game.start_game()