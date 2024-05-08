import pygame
import sys
from pygame.locals import *
from math import *
import time
import random
from config import *
import math

def rotate_coordinates(x_center, y_center, x, y, radius, angle):
    if x_center == x:
        return x, y
    theta = math.pi - math.atan((y-y_center)/(x-x_center)) - angle
    x2 = x_center - radius * math.cos(theta)
    y2 = y_center + radius * math.sin(theta)
    return x2, y2


class Bullet():
    """Note: the pathways for different bullet shape is completely different. BE WARNED"""
    def __init__(self, x, y, speed, color, angle, dimensions, damage):
        # self.symbol = bullet_symbol
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = angle
        self.color = color
        self.angle = angle
        self.damage = damage

        # Circular pathway
        if len(dimensions) == 1:
            self.radius = dimensions[0]
            self.SHAPE = "CIRCULAR"
        # Rectangular pathway
        if len(dimensions) == 2:
            self.width, self.height = dimensions[0], dimensions[1]

            theta = math.atan(self.width/self.height)
            length = (self.width**2 + self.height**2)**0.5 / 2
            self.x1 = x + length * math.cos(angle-theta)
            self.y1 = y + length * math.sin(angle-theta)
            self.x2 = x + length * math.cos(angle+theta)
            self.y2 = y + length * math.sin(angle+theta)
            self.x3 = x + length * math.cos(math.pi+angle-theta)
            self.y3 = y + length * math.sin(math.pi+angle-theta)
            self.x4 = x + length * math.cos(math.pi+angle+theta)
            self.y4 = y + length * math.sin(math.pi+angle+theta)

            self.length = length
            self.radius = min((self.width, self.height))

            self.SHAPE = "RECTANGULAR"

        print(self.SHAPE)
        print(self.angle)

    def update(self, player):
        """Update position of the bullet"""
        self.y += self.speed * cos(self.angle)
        self.x += self.speed * sin(self.angle)

        # Make sure to include this block of shit everytime you override update
        if self.SHAPE == "RECTANGULAR":
            self.y1 += self.speed * cos(self.angle)
            self.x1 += self.speed * sin(self.angle)
            self.y2 += self.speed * cos(self.angle)
            self.x2 += self.speed * sin(self.angle)
            self.y3 += self.speed * cos(self.angle)
            self.x3 += self.speed * sin(self.angle)
            self.y4 += self.speed * cos(self.angle)
            self.x4 += self.speed * sin(self.angle)

    def draw(self, screen):
        if self.SHAPE == "CIRCULAR":
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        if self.SHAPE == "RECTANGULAR":
            point_lst = ((self.x1, self.y1), (self.x2, self.y2), (self.x3, self.y3), (self.x4, self.y4))
            pygame.draw.polygon(screen, self.color, point_lst)

    def check_collision(self, target):

        if self.SHAPE == "CIRCULAR":
            distance_x = self.x - (target.x + target.width / 2)
            distance_y = self.y - (target.y + target.height / 2)
            distance = sqrt(distance_x ** 2 + distance_y ** 2)

            # Check if the distance is less than the sum of the bullet's radius and half of the player's width/height
            if distance < (self.radius + max(target.width, target.height) / 2):
                return True
            else:
                return False

        if self.SHAPE == "RECTANGULAR":
            x1, y1 = rotate_coordinates(self.x, self.y, self.x1, self.y1, self.length, -self.angle)
            x2, y2 = rotate_coordinates(self.x, self.y, self.x2, self.y2, self.length, -self.angle)
            x3, y3 = 2*self.x-x1, 2*self.y-y1
            x4, y4 = 2*self.x-x2, 2*self.y-y2

            # Convert target coordinates
            radius = ((target.x+target.radius-self.x)**2 + (target.y+target.radius-self.y)**2) ** 0.5
            x_target, y_target = rotate_coordinates(self.x, self.y, target.x+target.radius, target.y+target.radius, radius, -self.angle)

            # Calculate distance
            upper_left = (min([x1,x2,x3,x4]), min([y1,y2,y3,y4]))
            lower_right = (max([x1,x2,x3,x4]), max([y1,y2,y3,y4]))

            if x_target < lower_right[0]+target.radius and x_target > upper_left[0]-target.radius:
                # Check pygame coordinates
                if y_target > upper_left[1]-target.radius and y_target < lower_right[1]+target.radius:
                    return True
                else:
                    return False
            else:
                return False


class Tracking_Bullet(Bullet):
    def __init__(self, x, y, speed, color, angle, dimensions, track, target, damage):
        super().__init__(x, y, speed, color, angle, dimensions, damage)

        if self.angle > math.pi:
            while self.angle > math.pi:
                self.angle -= 2 * math.pi
        elif self.angle <= -math.pi:
            while self.angle < math.pi:
                self.angle += 2 * math.pi

        self.track = track
        self.target = target

    def update(self, player):
        if self.y == self.target.y:
            target_angle = self.angle # Placeholder to prevent 0 division
        else:
            target_angle = math.atan(((self.target.x+self.target.width/2)-self.x)/((self.target.y+self.target.height/2)-self.y))

        if self.angle == 0:  # Prevent 0 division
            if target_angle > self.angle:
                self.angle = min(target_angle, self.angle+self.track)
            if target_angle < self.angle:
                self.angle = max(target_angle, self.angle-self.track)
        else:
            if target_angle < self.angle:
                self.angle = max(target_angle, self.angle-self.track)
            else:
                self.angle = min(target_angle, self.angle+self.track)


        self.y += self.speed * cos(self.angle)
        self.x += self.speed * sin(self.angle)

        if self.SHAPE == "RECTANGULAR":
            self.y1 += self.speed * cos(self.angle)
            self.x1 += self.speed * sin(self.angle)
            self.y2 += self.speed * cos(self.angle)
            self.x2 += self.speed * sin(self.angle)
            self.y3 += self.speed * cos(self.angle)
            self.x3 += self.speed * sin(self.angle)
            self.y4 += self.speed * cos(self.angle)
            self.x4 += self.speed * sin(self.angle)


class Boss_Bullet(Bullet):
    def update(self, player):
        self.y += self.speed * cos(self.angle)
        self.x += self.speed * sin(self.angle)

class Boss_8_Split_Bullet(Bullet):  # DONE
    def update(self, player):
        super().update(player)
        if self.y < 0 or self.y > screen_height or self.x < 0 or self.x > screen_width:
            self.split()
            boss_bullets.remove(self)

    def split(self):
        for i in range(1,11):
            boss_bullets.append(Boss_Bullet(self.x * 0.99, self.y * 0.99, 4, WHITE, self.angle + pi/5 * i, [5], 10))

class Boss_Slow_Down_Bullet(Bullet):  # DONE
    def __init__(self, x, y, speed, color, angle, dimensions, acc, damage):
        super().__init__(x, y, speed, color, angle, dimensions, damage)
        self.acceleration = acc

    def update(self, player):
        self.y += self.speed * cos(self.angle)
        self.x += self.speed * sin(self.angle)
        self.speed += self.acceleration
        if self.speed <= 0:
            boss_bullets.remove(self)


class Boss_Shatter_Explosion_Bullet(Boss_Slow_Down_Bullet, Boss_8_Split_Bullet):  # DONE
    triggered_time = None
    def minor_split(self):
        for i in range(1,7):
            boss_bullets.append(Boss_Bullet(self.x * 0.99, self.y * 0.99, 4, WHITE, self.angle + pi/3 * i, [5], damage=10))
    def update(self, player):
        if self.triggered_time is None:
            if self.speed > 0:
                self.y += self.speed * cos(self.angle)
                self.x += self.speed * sin(self.angle)
                self.speed += self.acceleration
            else:
                self.speed = 0
                self.color = RED
                self.triggered_time = pygame.time.get_ticks()
        if self.triggered_time is not None:
            if pygame.time.get_ticks() - self.triggered_time >= 2000:
                self.split()
                if self in boss_bullets:
                    boss_bullets.remove(self)
        # 检查Far Collision
        if self.check_far_collision(player) or (
                self.y < 0 or self.y > screen_height or self.x < 0 or self.x > screen_width):
            self.minor_split()
            if self in boss_bullets:
                boss_bullets.remove(self)
    def check_far_collision(self, target):
        # Calculate the distance between the center of the bullet and the center of the player
        distance_x = self.x - (target.x + target.width / 2)
        distance_y = self.y - (target.y + target.height / 2)
        distance = sqrt(distance_x ** 2 + distance_y ** 2)

        # Check if the distance is less than the sum of the bullet's radius and half of the player's width/height
        if distance < (self.radius + max(target.width, target.height) / 2) * 10:
            return True
        else:
            return False
