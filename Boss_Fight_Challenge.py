import pygame
import sys, os
from pygame.locals import *
from math import *
import time
import random
from Danmaku import *
from Movement import *
from Bullet_Collection import *
from Sprites import *
from config import *
import inspect
# 
# # 游戏窗口尺寸
# screen_width = 600
# screen_height = 800
#
# # 定义颜色
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# ENEMY_COLOR = (128, 64, 200)
# BOSS_COLOR = (176, 120, 50)


def game(screen):
    # 创建玩家对象
    global player
    player = Player(screen_width // 2 - 10, screen_height - 40, 5, 100)  # TODO: may need to change health and stuffs

    # 创建Boss对象
    boss = Boss(screen_width // 2 - 20, screen_height // 2 - 270, 2, 1000)
    boss_marker = Boss_Marker(boss)

    # 游戏主循环
    clock = pygame.time.Clock()

    game_over = False


    while not game_over:
        screen.fill(BLACK)

        # 存储需要移除的子弹
        bullets_to_remove = []

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    player.shooting = True

            if event.type == KEYUP:
                if event.key == K_SPACE:
                    player.shooting = False

        if player.shooting:
            player.shoot(boss)

        if not game_over:
            player.update()
            player.draw(screen)

            for bullet in bullets:
                bullet.update(player)
                bullet.draw(screen)

                # 检查子弹是否击中Boss
                if bullet.check_collision(boss):
                    if inspect.isclass(Bullet):
                        boss.health -= 2
                    elif inspect.isclass(Tracking_Bullet):
                        boss.health -= 1.5
                    if boss.health <= 0:
                        print('Won')
                        game_over = True
                    if bullet not in bullets_to_remove:
                        bullets_to_remove.append(bullet)

                # 检查子弹是否超出屏幕
                if bullet.y < 0 or bullet.y > screen_height or bullet.x < 0 or bullet.x > screen_width:
                    if bullet not in bullets_to_remove:
                        bullets_to_remove.append(bullet)

            # 移除需要移除的子弹
            for bullet in bullets_to_remove:
                bullets.remove(bullet)


            for boss_bullet in boss_bullets:
                boss_bullet.update(player)
                boss_bullet.draw(screen)

                # 检查Boss子弹是否击中玩家
                if boss_bullet.check_collision(player):
                    player.health -= boss_bullet.damage
                    boss_bullets.remove(boss_bullet)

                # 检查Boss子弹是否超出屏幕
                if boss_bullet.y < 0 or boss_bullet.y > screen_height or boss_bullet.x < 0 or boss_bullet.x > screen_width:
                    if boss_bullet in boss_bullets:
                        boss_bullets.remove(boss_bullet)

            boss.update()
            boss.draw(screen)

            boss_marker.update()
            boss_marker.draw(screen)

            # 检查Boss是否与玩家碰撞
            if player.x < boss.x + boss.width and player.x + player.width > boss.x and player.y < boss.y + boss.height and player.y + player.height > boss.y:
                player.health -= 20
                if boss.health <= 0:
                    print('Won')
                    game_over = True
                print('Lost')
                game_over = True

            # 检查玩家生命值
            if player.health <= 0:
                print('Lost')
                game_over = True

        pygame.display.flip()
        print(len(boss_bullets), len(bullets))
        clock.tick(60)

    # pygame.quit()

if __name__ == '__main__':
    screen_position = (screen_width - 100, screen_height // 2 - 380)
    os.environ['SDL_VIDEO_WINDOW_POS'] = "{},{}".format(screen_position[0], screen_position[1])
    # 初始化Pygame
    pygame.init()

    # 创建游戏窗口
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Bullet Hell Game")

    game(screen)
