import pygame
import sys
from pygame.locals import *
from math import *
import time
import random
import config
from sympy import symbols, diff


def M_infinity_movement(self):  # Move in a ∞ shape
    return

def M_circle_movement(self, radius, rotation):  # Move in a circle. Starts from the top of the circle.
    self.M_circle_temp_count += rotation
    self.move_angle(radius, self.M_circle_temp_count)