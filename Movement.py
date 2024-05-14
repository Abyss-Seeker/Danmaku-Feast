import pygame
import sys
from pygame.locals import *
from math import *
import time
import random
import config
from sympy import symbols, diff

def M_infinity_movement(self, speed, magnitude):  # Move in a ∞ shape
    # Update the internal counter for the movement
    self.M_infinity_temp_count += speed

    # Parametric equations for the infinity shape
    t = self.M_infinity_temp_count
    x = magnitude * cos(t)
    y = magnitude * sin(2 * t - pi/2) / 2

    # Move the object based on the parametric equations
    self.move(x, y)

def M_circle_movement(self, radius, rotation):  # Move in a circle. Starts from the top of the circle.
    self.M_circle_temp_count += rotation
    self.move_angle(radius, self.M_circle_temp_count)
