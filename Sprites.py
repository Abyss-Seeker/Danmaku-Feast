import pygame
import sys
from pygame.locals import *
from math import *
import time
import random
import config
from Bullet_Collection import *
from Danmaku import *
from Movement import *


class Player:
    def __init__(self, x, y, speed, health):
        # self.symbol = player_symbol
        self.x = x
        self.y = y
        self.speed = speed
        self.SPEED = speed
        self.health = health
        self.HEALTH = health
        self.width = 10
        self.height = 10
        self.shooting = False
        self.last_shot = pygame.time.get_ticks()
        self.shoot_delay = 50
        config.Player_width = self.width
        config.Player_height = self.height


    def move(self, keys):
        # Initialize movement vector
        move_vector = [0, 0]

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            move_vector[0] -= 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            move_vector[0] += 1
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            move_vector[1] -= 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            move_vector[1] += 1

        # Normalize the vector
        magnitude = sqrt(move_vector[0] ** 2 + move_vector[1] ** 2)
        if magnitude != 0:
            normalized_vector = [move_vector[0] / magnitude, move_vector[1] / magnitude]
        else:
            normalized_vector = [0, 0]

        # Update player position
        if not (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]):
            self.x += normalized_vector[0] * self.speed
            self.y += normalized_vector[1] * self.speed
        else:
            self.x += normalized_vector[0] * self.speed / 2
            self.y += normalized_vector[1] * self.speed / 2


    def update(self):
        keys = pygame.key.get_pressed()
        self.move(keys)

        if self.x < 0:
            self.x = 0
        if self.x > screen_width - self.width:
            self.x = screen_width - self.width
        if self.y < 0:
            self.y = 0
        if self.y > screen_height - self.height:
            self.y = screen_height - self.height

        config.Player_x = self.x
        config.Player_y = self.y
        # print(Player_x, Player_y)

    def draw(self, screen):
        pygame.draw.rect(screen, PLAYER_COLOR, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, GREEN, (self.x, self.y - 10, (self.width / self.HEALTH) * self.health, 5))

    def shoot(self, target):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot > self.shoot_delay:
            bullet = Bullet(self.x+self.width//2, self.y-10, -35, PLAYER_COLOR, 0, [6.5, 4.5], 2)
            bullets.append(bullet)
            bullet = Tracking_Bullet(self.x+self.width//2, self.y-10, -15, BLUE, -0.1, [3.5], 0.01, target, 1.5)
            bullets.append(bullet)
            bullet = Tracking_Bullet(self.x+self.width//2, self.y-10, -15, BLUE, 0.1, [3.5], 0.01, target, 1.5)
            bullets.append(bullet)

            self.last_shot = current_time

    def reset(self):
        self.x = screen_width // 2 - self.width // 2
        self.y = screen_height - self.height - 10
        self.speed = 5
        self.health = 100

# 创建Boss类
class Boss:
    def __init__(self, x, y, speed, health):
        # self.symbol = boss_symbol
        self.x = x
        self.y = y
        self.speed = speed
        self.health = health
        self.width = 40
        self.height = 40
        self.chance = 1
        self.HEALTH = health
        self.S_bullet_angle = 0
        self.attack = 1  # FIXME: THIS IS WHERE YOU DEBUG THE LEVELS, NEEDS TO BE CHANGED IN LATER UPDATES
        # For S_spray
        self.S_temp = 0
        self.S_temp_count = 0
        self.S_temp_count_frequency_modifier = 0
        # For S_spray_2
        self.S_temp_count_frequency_modifier_2 = 0
        self.S_temp_2 = 0
        self.S_temp_count_2 = 0
        self.S_flag_2 = 1
        # For S_split
        self.S_temp_count_frequency_modifier_split = 0
        # For S_slow_down_shot
        self.S_temp_count_frequency_modifier_slow_down = 0
        # For M_infinity_movement
        self.M_infinity_temp_count = 0
        # For M_circle_movement
        self.M_circle_temp_count = 0
        # 好笑的
        self.radius = min([self.width, self.height]) / 2

    # For resetting variables
    def S_spray_variable_reset(self):
        self.S_temp = 0
        self.S_temp_count = 0
        self.S_temp_count_frequency_modifier = 0

    def S_spray_2_variable_reset(self):
        self.S_temp_count_frequency_modifier_2 = 0
        self.S_temp_2 = 0
        self.S_temp_count_2 = 0
        self.S_flag_2 = 1

    def S_split_variable_reset(self):
        self.S_temp_count_frequency_modifier_split = 0

    def S_slow_down_shot_variable_reset(self):
        self.S_temp_count_frequency_modifier_slow_down = 0

    def M_infinity_movement_variable_reset(self):
        self.M_infinity_temp_count = 0

    def M_circle_movement_variable_reset(self):
        self.M_circle_temp_count = 0

    def update(self):
        current_time = pygame.time.get_ticks()
        # print(current_time)
        # self.x += self.speed
        # if self.x < 0 or self.x > screen_width - self.width:
        #     self.speed *= -1
        if self.health <= self.HEALTH:
            if self.health + 0.5 <= self.HEALTH:
                self.health += 0.5
            else:
                self.health += self.HEALTH - self.health
        if self.attack == 0:  # FIXME: FOR MODIFYING THE DANMAKU ATTACK PATTERNS
            # self.S_spray_variable_reset()
            # self.S_slow_down_shot_variable_reset()
            # self.M_infinity_movement_variable_reset()
            M_infinity_movement(self, speed=0.02, magnitude=2)
            S_spray(self)
            S_slow_down_shotgun(self, 150, 10, 5.5, 8)
        elif self.attack == 1:
            # self.S_spray_2_variable_reset()
            # self.S_slow_down_shot_variable_reset()
            M_infinity_movement(self, speed=0.02, magnitude=2)
            S_spray_2(self)
            S_slow_down_shotgun(self, 150, 10, 5.5, 8)
        elif self.attack == 2:
            # self.S_split_variable_reset()
            S_split(self)
            # S_spray(self)
            # S_spray_2(self
        elif self.attack == 3:
            # self.S_slow_down_shot_variable_reset()
            S_slow_down_shotgun(self, 50, 10, 5.5, 8)
        elif self.attack == 4:
            # self.S_split_variable_reset()
            S_shatter_explosion(self)


    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, GREEN, (self.x, self.y - 10, (self.width / self.HEALTH) * self.health, 5))

    def reset(self):
        self.x = screen_width // 2 - self.width // 2
        self.y = 50
        self.speed = random.choice([-1, 1])
        self.health = 200

    def shoot(self, boss_bullet):
        boss_bullets.append(boss_bullet)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_angle(self, magnitude, angle):
        angle_rad = math.radians(angle)
        dx = magnitude * math.cos(angle_rad)
        dy = magnitude * math.sin(angle_rad)
        self.x += dx
        self.y += dy


class Boss_Marker:
    def __init__(self, boss):
        self.boss = boss
        self.size = 25
        self.color = BLUE

    def update(self):
        # Update the position of the marker based on the boss's position
        self.x = self.boss.x + self.boss.width / 2 - self.size / 2
        self.y = screen_height - self.size

    def draw(self, screen):
        # Draw the diamond marker on the screen
        pygame.draw.polygon(screen, self.color, [
            (self.x + self.size / 2, self.y + self.size / 2),  # Top point
            (self.x - self.size / 2, self.y + self.size),  # Left point
            (self.x + self.size / 2, self.y + self.size * 1.5),  # Bottom point
            (self.x + self.size * 1.5, self.y + self.size)  # Right point
        ])


