import pygame
import sys
from pygame.locals import *
from math import *
import time
import random
import config
from Bullet_Collection import *
from Bullet_Collection import Boss_Shatter_Explosion_Bullet
# import Boss_Fight_Challenge




def S_spray(self):  # DONE
    self.S_temp_count_frequency_modifier += 1
    if self.S_temp_count_frequency_modifier % 6 == 0:
        self.S_temp_count += 1
        if self.S_temp_count % 200 == self.S_temp_count % 400:
            self.S_temp += 0.009
        else:
            self.S_temp -= 0.009
        self.S_bullet_angle += self.S_temp ** 2 - self.S_temp + 0.01
        self.shoot(Boss_Bullet(self.x+self.width/2, self.y+self.height/2, speed=5, color=WHITE, angle=self.S_bullet_angle, dimensions=[5], damage=10))
    elif self.S_temp_count_frequency_modifier % 6 == 1:
        self.shoot(Boss_Bullet(self.x + self.width / 2, self.y + self.height / 2, speed=5, color=WHITE,
                               angle=(self.S_bullet_angle + 1 * pi / 3), dimensions=[5], damage=10))
    elif self.S_temp_count_frequency_modifier % 6 == 2:
        self.shoot(Boss_Bullet(self.x + self.width / 2, self.y + self.height / 2, speed=5, color=WHITE,
                               angle=(self.S_bullet_angle + 2 * pi / 3), dimensions=[5], damage=10))
    elif self.S_temp_count_frequency_modifier % 6 == 3:
        self.shoot(Boss_Bullet(self.x + self.width / 2, self.y + self.height / 2, speed=5, color=WHITE,
                               angle=(self.S_bullet_angle + 3 * pi / 3), dimensions=[5], damage=10))
    elif self.S_temp_count_frequency_modifier % 6 == 4:
        self.shoot(Boss_Bullet(self.x + self.width / 2, self.y + self.height / 2, speed=5, color=WHITE,
                               angle=(self.S_bullet_angle + 4 * pi / 3), dimensions=[5], damage=10))
    elif self.S_temp_count_frequency_modifier % 6 == 5:
        self.shoot(Boss_Bullet(self.x + self.width / 2, self.y + self.height / 2, speed=5, color=WHITE,
                               angle=(self.S_bullet_angle + 5 * pi / 3), dimensions=[5], damage=10))

def S_spray_2(self):  # DONE
    if self.S_temp_count_frequency_modifier_2 > 2200:
        self.S_flag_2 = 0
    if self.S_temp_count_frequency_modifier_2 < 0:
        self.S_flag_2 = 1
    # print(self.S_flag_2, self.S_temp_count_frequency_modifier_2)
    if self.S_flag_2:
        self.S_temp_count_frequency_modifier_2 += 1
    else:
        self.S_temp_count_frequency_modifier_2 -= 1
    self.S_temp_count_2 += 0.01
    if self.S_temp_count_frequency_modifier_2 < 500:
        if self.S_temp_count_frequency_modifier_2 % 4 == 0:
            self.S_bullet_angle_2 = self.S_temp_count_2  * sin(self.S_temp_count_2)
            self.shoot(Boss_Bullet(self.x + self.width / 2, self.y + self.height / 2, speed=5, color=WHITE,
                                   angle=self.S_bullet_angle_2, dimensions=[5], damage=10))
    elif self.S_temp_count_frequency_modifier_2 < 1000:
        if self.S_temp_count_frequency_modifier_2 % 4 == 0:
            self.S_bullet_angle_2 = self.S_temp_count_2  * sin(self.S_temp_count_2)
            self.shoot(Boss_Bullet(self.x + self.width / 2, self.y + self.height / 2, speed=5, color=WHITE,
                                   angle=self.S_bullet_angle_2, dimensions=[5], damage=10))
            self.S_bullet_angle_2 = (self.S_temp_count_2-5) * cos(self.S_temp_count_2-5)
            self.shoot(Boss_Bullet(self.x + self.width / 2, self.y + self.height / 2, speed=5, color=WHITE,
                                   angle=self.S_bullet_angle_2, dimensions=[5], damage=10))
    elif self.S_temp_count_frequency_modifier_2 < 1500:
        if self.S_temp_count_frequency_modifier_2 % 4 == 0:
            self.S_bullet_angle_2 = self.S_temp_count_2  * sin(self.S_temp_count_2)
            self.shoot(Boss_Bullet(self.x + self.width / 2, self.y + self.height / 2, speed=5, color=WHITE,
                                   angle=self.S_bullet_angle_2, dimensions=[5], damage=10))
            self.S_bullet_angle_2 = (self.S_temp_count_2-5) * cos(self.S_temp_count_2-5)
            self.shoot(Boss_Bullet(self.x + self.width / 2, self.y + self.height / 2, speed=5, color=WHITE,
                                   angle=self.S_bullet_angle_2, dimensions=[5], damage=10))
            self.S_bullet_angle_2 = (self.S_temp_count_2-10) * tan(self.S_temp_count_2-10)
            self.shoot(Boss_Bullet(self.x + self.width / 2, self.y + self.height / 2, speed=5, color=WHITE,
                                   angle=self.S_bullet_angle_2, dimensions=[5], damage=10))
    else:
        if self.S_temp_count_frequency_modifier_2 % 6 == 0:
            self.S_bullet_angle_2 = self.S_temp_count_2  * sin(self.S_temp_count_2)
            self.shoot(Boss_Bullet(self.x + self.width / 2, self.y + self.height / 2, speed=5, color=WHITE,
                                   angle=self.S_bullet_angle_2, dimensions=[5], damage=10))
            self.S_bullet_angle_2 = (self.S_temp_count_2-5) * cos(self.S_temp_count_2-5)
            self.shoot(Boss_Bullet(self.x + self.width / 2, self.y + self.height / 2, speed=5, color=WHITE,
                                   angle=self.S_bullet_angle_2, dimensions=[5], damage=10))
            self.S_bullet_angle_2 = (self.S_temp_count_2-10) * tan(self.S_temp_count_2-10)
            self.shoot(Boss_Bullet(self.x + self.width / 2, self.y + self.height / 2, speed=5, color=WHITE,
                                   angle=self.S_bullet_angle_2, dimensions=[5], damage=10))
            self.S_bullet_angle_2 = - self.S_temp_count_2 * sin(self.S_temp_count_2)
            self.shoot(Boss_Bullet(self.x + self.width / 2, self.y + self.height / 2, speed=5, color=WHITE,
                                   angle=self.S_bullet_angle_2, dimensions=[5], damage=10))
            self.S_bullet_angle_2 = - (self.S_temp_count_2-5) * cos(self.S_temp_count_2-5)
            self.shoot(Boss_Bullet(self.x + self.width / 2, self.y + self.height / 2, speed=5, color=WHITE,
                                   angle=self.S_bullet_angle_2, dimensions=[5], damage=10))
            self.S_bullet_angle_2 = - (self.S_temp_count_2-10) * tan(self.S_temp_count_2-10)
            self.shoot(Boss_Bullet(self.x + self.width / 2, self.y + self.height / 2, speed=5, color=WHITE,
                                   angle=self.S_bullet_angle_2, dimensions=[5], damage=10))


def S_split(self):  # DONE
    self.S_temp_count_frequency_modifier_split += 1
    if self.S_temp_count_frequency_modifier_split % 15 == 0:
        self.shoot(Boss_8_Split_Bullet(self.x + self.width / 2, self.y + self.height / 2, 5, WHITE, random.uniform(0, 2*pi), [7], damage=20))


def S_slow_down_shotgun(self, freq, density, size, speed):  # DONE
    self.S_temp_count_frequency_modifier_slow_down += 1
    # print(Player_x, Player_width)
    angle = atan(((config.Player_x + config.Player_width / 2) - (self.x + self.width / 2)) / (
                (config.Player_y + config.Player_height / 2) - (self.y + self.width / 2)))
    if (config.Player_y + config.Player_height / 2) - (self.y + self.width / 2) <= 0:
        angle += pi
    if self.S_temp_count_frequency_modifier_slow_down % freq == 0:
        # print(angle)
        for i in range(density):
            self.shoot(Boss_Slow_Down_Bullet(self.x + self.width / 2, self.y + self.height / 2, speed * random.uniform(0.8, 1.2), WHITE, angle + random.uniform(-0.1,0.1), [size * random.uniform(0.8,1.2)], -0.033, damage=10))

def S_shatter_explosion(self):  # DONE
    self.S_temp_count_frequency_modifier_split += 1
    angle = atan(((config.Player_x + config.Player_width / 2) - (self.x + self.width / 2)) / (
                (config.Player_y + config.Player_height / 2) - (self.y + self.width / 2)))
    if self.S_temp_count_frequency_modifier_split % 25 == 0:
        self.shoot(Boss_Shatter_Explosion_Bullet(self.x+self.width/2, self.y+self.height/2, 6*random.uniform(0.6, 1.2), WHITE,
                                                        angle+random.uniform(-0.3,0.3), [7], -0.033 * random.uniform(0.75, 1.25), damage=20))

def S_glider(self):  # DONE
    self.S_temp_count_frequency_modifier_glider += 1
    if self.S_temp_count_frequency_modifier_glider % 15 == 0:
        self.shoot(Boss_Glider_Bullet(self.x + self.width / 2, self.y + self.height / 2, 5, WHITE, random.uniform(0, 2*pi), [7], damage=20, freq= 20))

def S_skimmer(self):  # DONE
    self.S_temp_count_frequency_modifier_skimmer += 1
    if self.S_temp_count_frequency_modifier_skimmer % 40 == 0:
        self.shoot(Boss_Skimmer_Bullet(self.x + self.width / 2, self.y + self.height / 2, 2, WHITE, random.uniform(0, 2*pi), [7], damage=20, freq= 10, angle_velo=0.033))

# TODO: Every time a new danmaku is added, put it's attack index into the dictionary; see Sprites.py file
danmaku_name = {
    "Spray danmaku": 0,
    "Spray danmaku 2": 1,
    "Split danmaku": 2,
    "Shotgun danmaku": 3,
    "Explosion danmaku": 4,
    "Glider danmaku": 5,
    "Skimmer danmaku": 6
}