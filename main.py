import pygame
import sys
from pygame.locals import *
from math import *
from Sprites import Boss_Marker

def spring01():
    # 初始化Pygame
    pygame.init()

    # 设置窗口尺寸
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600

    # 设置颜色
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)

    # 设置弹簧参数
    SPRING_WIDTH = 200
    SPRING_HEIGHT = 20
    SPRING_COLOR = BLUE
    SPRING_STIFFNESS = 0.05
    SPRING_DAMPING = 0.05

    # 设置圆形参数
    CIRCLE_RADIUS = 40
    CIRCLE_COLOR = BLUE
    CIRCLE_MASS = 1.0
    CIRCLE_DRAG = 0.95

    # 创建窗口
    window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Spring Simulation')

    # 创建时钟对象
    clock = pygame.time.Clock()

    # 设置初始位置和速度
    circle_pos = [WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2]
    circle_velocity = [0, 0]

    # 辅助函数：计算两点之间的距离
    def distance(p1, p2):
        return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    # 游戏主循环
    while True:
        # 处理退出事件
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # 清空窗口
        window_surface.fill(WHITE)

        # 获取鼠标位置
        mouse_pos = pygame.mouse.get_pos()

        # 计算弹簧向量和长度
        spring_vector = [circle_pos[0] - mouse_pos[0], circle_pos[1] - mouse_pos[1]]
        spring_length = distance(circle_pos, mouse_pos)

        # 计算弹簧力和阻尼力
        spring_force = [-SPRING_STIFFNESS * spring_vector[0] - SPRING_DAMPING * circle_velocity[0],
                        -SPRING_STIFFNESS * spring_vector[1] - SPRING_DAMPING * circle_velocity[1]]

        # 更新速度和位置
        circle_velocity[0] += spring_force[0] / CIRCLE_MASS
        circle_velocity[1] += spring_force[1] / CIRCLE_MASS
        circle_velocity[0] *= CIRCLE_DRAG
        circle_velocity[1] *= CIRCLE_DRAG
        circle_pos[0] += circle_velocity[0]
        circle_pos[1] += circle_velocity[1]

        # 绘制弹簧
        pygame.draw.line(window_surface, SPRING_COLOR, mouse_pos, circle_pos, SPRING_HEIGHT)

        # 绘制圆形
        pygame.draw.circle(window_surface, CIRCLE_COLOR, (int(circle_pos[0]), int(circle_pos[1])), CIRCLE_RADIUS)

        # 刷新窗口
        pygame.display.update()
        clock.tick(60)

def spring02():
    # 初始化Pygame
    pygame.init()

    # 设置窗口尺寸
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600

    # 设置颜色
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)

    # 设置弹簧参数
    SPRING_WIDTH = 200
    SPRING_HEIGHT = 20
    SPRING_COLOR = BLUE
    SPRING_STIFFNESS = 0.05
    SPRING_DAMPING = 0.05

    # 设置圆形参数
    CIRCLE_RADIUS = 40
    CIRCLE_COLOR = BLUE
    CIRCLE_MASS = 1.0
    CIRCLE_DRAG = 0.95

    # 设置重力参数
    GRAVITY = 0.5

    # 创建窗口
    window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Spring Simulation')

    # 创建时钟对象
    clock = pygame.time.Clock()

    # 设置初始位置和速度
    circle_pos = [WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2]
    circle_velocity = [0, 0]  # 将此处的括号改为方括号，定义为列表

    # 设置弹簧固定点
    spring_fixed_pos = [WINDOW_WIDTH // 2, WINDOW_HEIGHT - SPRING_HEIGHT - CIRCLE_RADIUS]

    # 辅助函数：计算两点之间的距离
    def distance(p1, p2):
        return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    # 游戏主循环
    dragging = False  # 是否正在拖拽圆球
    while True:
        # 处理退出事件
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                # 鼠标左键按下，开始拖拽圆球
                mouse_pos = pygame.mouse.get_pos()
                if distance(mouse_pos, circle_pos) <= CIRCLE_RADIUS:
                    dragging = True
            elif event.type == MOUSEBUTTONUP and event.button == 1:
                # 鼠标左键松开，停止拖拽圆球
                dragging = False

        # 清空窗口
        window_surface.fill(WHITE)

        # 获取鼠标位置
        mouse_pos = list(pygame.mouse.get_pos())

        # 如果正在拖拽圆球，更新圆球位置为鼠标位置
        if dragging:
            circle_pos = mouse_pos

        # 计算弹簧向量和长度
        spring_vector = [circle_pos[0] - spring_fixed_pos[0], circle_pos[1] - spring_fixed_pos[1]]
        spring_length = max(distance(circle_pos, spring_fixed_pos), CIRCLE_RADIUS + SPRING_HEIGHT)

        # 计算弹簧力和阻尼力
        spring_force = [-SPRING_STIFFNESS * spring_vector[0] - SPRING_DAMPING * circle_velocity[0],
                        -SPRING_STIFFNESS * spring_vector[1] - SPRING_DAMPING * circle_velocity[1]]

        # 计算重力
        gravity_force = [0, CIRCLE_MASS * GRAVITY]

        # 更新速度和位置
        if not dragging:
            circle_velocity[0] += (spring_force[0] + gravity_force[0]) / CIRCLE_MASS
            circle_velocity[1] += (spring_force[1] + gravity_force[1]) / CIRCLE_MASS
            circle_velocity[0] *= CIRCLE_DRAG
            circle_velocity[1] *= CIRCLE_DRAG
            circle_pos[0] += circle_velocity[0]
            circle_pos[1] += circle_velocity[1]

        # 绘制弹簧
        pygame.draw.line(window_surface, SPRING_COLOR, (spring_fixed_pos[0], spring_fixed_pos[1] + CIRCLE_RADIUS), circle_pos, SPRING_HEIGHT)

        # 绘制圆形
        pygame.draw.circle(window_surface, CIRCLE_COLOR, (int(circle_pos[0]), int(circle_pos[1])), CIRCLE_RADIUS)

        # 绘制地面
        pygame.draw.line(window_surface, BLUE, (0, WINDOW_HEIGHT - SPRING_HEIGHT), (WINDOW_WIDTH, WINDOW_HEIGHT - SPRING_HEIGHT), 2)

        # 刷新窗口
        pygame.display.update()
        clock.tick(60)

def spring03():
    # 初始化Pygame
    pygame.init()

    # 设置窗口尺寸
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600

    # 设置颜色
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)

    # 设置弹簧参数
    SPRING_WIDTH = 200
    SPRING_HEIGHT = 20
    SPRING_COLOR = BLUE
    SPRING_STIFFNESS = 0.05
    SPRING_DAMPING = 0.05

    # 设置圆形参数
    CIRCLE_RADIUS = 40
    CIRCLE_COLOR = BLUE
    CIRCLE_MASS = 1.0
    CIRCLE_DRAG = 0.95

    # 创建窗口
    window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Spring Simulation')

    # 创建时钟对象
    clock = pygame.time.Clock()

    # 设置初始位置和速度
    circle_pos = [WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2]
    circle_velocity = [0, 0]

    # 设置弹簧固定点
    spring_fixed_pos = [circle_pos[0], circle_pos[1]]

    # 辅助函数：计算两点之间的距离
    def distance(p1, p2):
        return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    # 游戏主循环
    dragging = False
    while True:
        # 处理退出事件
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                # 鼠标左键按下，开始拖拽圆球
                mouse_pos = pygame.mouse.get_pos()
                if distance(mouse_pos, circle_pos) <= CIRCLE_RADIUS:
                    dragging = True
            elif event.type == MOUSEBUTTONUP and event.button == 1:
                # 鼠标左键松开，停止拖拽圆球
                dragging = False

        # 清空窗口
        window_surface.fill(WHITE)

        # 获取鼠标位置
        mouse_pos = pygame.mouse.get_pos()

        # 如果正在拖拽圆球，更新圆球位置为鼠标位置
        if dragging:
            circle_pos = list(mouse_pos)  # 将元组转换为列表

        # 计算弹簧向量和长度
        spring_vector = [circle_pos[0] - spring_fixed_pos[0], circle_pos[1] - spring_fixed_pos[1]]
        spring_length = max(distance(circle_pos, spring_fixed_pos), CIRCLE_RADIUS + SPRING_HEIGHT)

        # 计算弹簧力和阻尼力
        spring_force = [-SPRING_STIFFNESS * spring_vector[0] - SPRING_DAMPING * circle_velocity[0],
                        -SPRING_STIFFNESS * spring_vector[1] - SPRING_DAMPING * circle_velocity[1]]

        # 更新速度和位置
        if not dragging:
            circle_velocity[0] += spring_force[0] / CIRCLE_MASS
            circle_velocity[1] += spring_force[1] / CIRCLE_MASS
            circle_velocity[0] *= CIRCLE_DRAG
            circle_velocity[1] *= CIRCLE_DRAG
            circle_pos[0] += circle_velocity[0]
            circle_pos[1] += circle_velocity[1]

        # 绘制弹簧
        pygame.draw.line(window_surface, SPRING_COLOR, (spring_fixed_pos[0], spring_fixed_pos[1] + CIRCLE_RADIUS),
                         circle_pos, SPRING_HEIGHT)

        # 绘制圆形
        pygame.draw.circle(window_surface, CIRCLE_COLOR, (int(circle_pos[0]), int(circle_pos[1])), CIRCLE_RADIUS)

        # 刷新窗口
        pygame.display.update()
        clock.tick(60)

def game():
    import pygame
    import random

    # 游戏窗口尺寸
    screen_width = 600
    screen_height = 800

    # 定义颜色
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    ENEMY_COLOR = (128, 64, 200)
    BOSS_COLOR = (176, 120, 50)

    # 初始化Pygame
    pygame.init()

    # 创建游戏窗口
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Bullet Hell Game")

    # 定义玩家和敌人的符号
    player_symbol = "O"
    enemy_symbol = "X"
    boss_symbol = "B"
    bullet_symbol = "."

    # 创建玩家类
    class Player:
        def __init__(self, x, y, speed, health):
            self.symbol = player_symbol
            self.x = x
            self.y = y
            self.speed = speed
            self.SPEED = speed
            self.health = health
            self.HEALTH = health
            self.width = 20
            self.height = 20
            self.shooting = False
            self.last_shot = pygame.time.get_ticks()
            self.shoot_delay = 100

        def update(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.x -= self.speed
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.x += self.speed
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                self.y -= self.speed
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.y += self.speed
            # if pygame.key.get_mods() == pygame.KMOD_SHIFT:
            #     self.speed = self.SPEED / 2
            # else:
            #     self.speed = self.SPEED

            if self.x < 0:
                self.x = 0
            if self.x > screen_width - self.width:
                self.x = screen_width - self.width
            if self.y < 0:
                self.y = 0
            if self.y > screen_height - self.height:
                self.y = screen_height - self.height

        def draw(self):
            pygame.draw.rect(screen, BOSS_COLOR, (self.x, self.y, self.width, self.height))
            pygame.draw.rect(screen, GREEN, (self.x, self.y - 10, (self.width / self.HEALTH) * self.health, 5))

        def shoot(self):
            current_time = pygame.time.get_ticks()
            if current_time - self.last_shot > self.shoot_delay:
                bullet = Bullet(self.x + self.width // 2, self.y - 10, -5, RED, 5, random.uniform(-0.2, 0.2))
                bullets.append(bullet)
                self.last_shot = current_time

        def reset(self):
            self.x = screen_width // 2 - self.width // 2
            self.y = screen_height - self.height - 10
            self.speed = 5
            self.health = 100

    # 创建敌人类
    class Enemy:
        def __init__(self, x, y, speed, health):
            self.symbol = enemy_symbol
            self.x = x
            self.y = y
            self.speed = speed
            self.health = health
            self.HEALTH = health
            self.width = 30
            self.height = 30

        def check_collision(self, target):
            if self.x + self.width >= target.x and self.x <= target.x + target.width and self.y + self.height >= target.y and self.y <= target.y + target.height:
                return True
            return False

        def update(self):
            self.y += self.speed
            if self.y > screen_height:
                self.reset()

        def draw(self):
            pygame.draw.rect(screen, ENEMY_COLOR, (self.x, self.y, self.width, self.height))
            pygame.draw.rect(screen, GREEN, (self.x, self.y - 10, (self.width / self.HEALTH) * self.health, 5))

        def shoot(self):
            bullet = BossBullet(self.x + self.width // 2, self.y + self.height + 10, 3, BLUE, 4, random.uniform(-0.4, 0.4))
            boss_bullets.append(bullet)

        def reset(self):
            self.x = random.randint(0, screen_width - self.width)
            self.y = random.randint(-screen_height, -self.height)
            self.speed = random.randint(1, 3)
            self.health = 100

    # 创建Boss类
    class Boss:
        def __init__(self, x, y, speed, health):
            self.symbol = boss_symbol
            self.x = x
            self.y = y
            self.speed = speed
            self.health = health
            self.width = 60
            self.height = 60
            self.chance = 1
            self.HEALTH = health

        def update(self):
            self.x += self.speed
            if self.x < 0 or self.x > screen_width - self.width:
                self.speed *= -1

            # Boss发射子弹
            if random.randint(1, 100) <= self.chance:
                self.shoot()
                if self.chance < 100:
                    self.chance += 0.05
                if random.random() <= 33 / self.chance:
                    enemy = Enemy(random.randint(0, screen_width - 30), random.randint(-screen_height, -30),
                                  random.randint(1, 3), 100)
                    enemies.append(enemy)

        def draw(self):
            pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))
            pygame.draw.rect(screen, GREEN, (self.x, self.y - 10, (self.width / self.HEALTH) * self.health, 5))

        def reset(self):
            self.x = screen_width // 2 - self.width // 2
            self.y = 50
            self.speed = random.choice([-1, 1])
            self.health = 200

        def shoot(self):
            bullet = BossBullet(self.x + self.width // 2, self.y + self.height + 10, 5, BLUE, 10, 0.2)
            boss_bullets.append(bullet)
            bullet = BossBullet(self.x + self.width // 2, self.y + self.height + 10, 5, BLUE, 10, 0)
            boss_bullets.append(bullet)
            bullet = BossBullet(self.x + self.width // 2, self.y + self.height + 10, 5, BLUE, 10, -0.2)
            boss_bullets.append(bullet)

    # 创建子弹类
    class Bullet:
        def __init__(self, x, y, speed, color, radius, angle):
            self.symbol = bullet_symbol
            self.x = x
            self.y = y
            self.speed = speed
            self.color = color
            self.radius = radius
            self.angle = angle

        def update(self):
            self.y += self.speed * cos(self.angle)
            self.x += self.speed * sin(self.angle)

        def draw(self):
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

        def check_collision(self, target):
            if self.x >= target.x and self.x <= target.x + target.width and self.y >= target.y and self.y <= target.y + target.height:
                return True
            return False

    # 创建Boss子弹类
    class BossBullet(Bullet):
        def update(self):
            self.y += self.speed * cos(self.angle)
            self.x += self.speed * sin(self.angle)

            # 检查Boss子弹是否击中玩家
            if self.check_collision(player):
                player.health -= 25
                boss_bullets.remove(self)

    # 创建玩家对象
    player = Player(screen_width // 2 - 15, screen_height - 40, 5, 100)

    # 创建敌人对象
    enemies = []
    for _ in range(30):  # 提高敌人刷新频率
        enemy = Enemy(random.randint(0, screen_width - 30), random.randint(-screen_height, -30), random.randint(1, 3), 100)
        enemies.append(enemy)

    # 创建Boss对象
    boss = Boss(screen_width // 2 - 30, 50, 2, 400)
    boss_marker = Boss_Marker(boss)

    # 存储子弹的列 表
    bullets = []
    boss_bullets = []  # 存储Boss子弹的列表

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
            player.shoot()

        if not game_over:
            player.update()
            player.draw()

            for bullet in bullets:
                bullet.update()
                bullet.draw()

                # 检查子弹是否击中敌人
                for enemy in enemies:
                    if bullet.check_collision(enemy):
                        enemy.health -= 50
                        if enemy.health <= 0:
                            enemies.remove(enemy)
                        if bullet not in bullets_to_remove:
                            bullets_to_remove.append(bullet)

                # 检查子弹是否击中Boss
                if bullet.check_collision(boss):
                    boss.health -= 10
                    if boss.health <= 0:
                        print('Won')
                        game_over = True
                    if bullet not in bullets_to_remove:
                        bullets_to_remove.append(bullet)

                # 检查子弹是否超出屏幕
                if bullet.y < 0 or bullet.y > screen_height:
                    if bullet not in bullets_to_remove:
                        bullets_to_remove.append(bullet)

            # 移除需要移除的子弹
            for bullet in bullets_to_remove:
                bullets.remove(bullet)

            for enemy in enemies:
                enemy.update()
                enemy.draw()

                # 检查敌人是否与玩家碰撞
                if player.x < enemy.x + enemy.width and player.x + player.width > enemy.x and player.y < enemy.y + enemy.height and player.y + player.height > enemy.y:
                    player.health -= 10
                    enemy.reset()

                # 敌人射击
                if random.randint(1, 100) == 1:
                    enemy.shoot()

                # 检查Enemy子弹是否击中玩家
                if enemy.check_collision(player):
                    player.health -= 10

            for boss_bullet in boss_bullets:
                boss_bullet.update()
                boss_bullet.draw()

                # 检查Boss子弹是否击中玩家
                if boss_bullet.check_collision(player):
                    player.health -= 10

                # 检查Boss子弹是否超出屏幕
                if boss_bullet.y < 0 or boss_bullet.y > screen_height:
                    boss_bullets.remove(boss_bullet)


            boss.update()
            boss.health += 0.05
            boss.draw()

            boss_marker.update()
            boss_marker.draw(screen)

            # 检查Boss是否与玩家碰撞
            if player.x < boss.x + boss.width and player.x + player.width > boss.x and player.y < boss.y + boss.height and player.y + player.height > boss.y:
                player.health -= 20
                if boss.health <= 0:
                    print('Won')
                    game_over = True
                boss.reset()

            # 检查玩家生命值
            if player.health <= 0:
                print('Lost')
                game_over = True

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

game()