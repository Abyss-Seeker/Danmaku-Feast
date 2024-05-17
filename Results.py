

import pygame
from pygame.locals import *
from config import *
from Starting_GUI import draw_text
from Starting_GUI import font_options, font_title


def game(screen, result):
    msg = "You won" if result == 1 else "You lost"

    while True:
        draw_text(msg, font_title, (255, 255, 255), screen, screen_width//2 - font_options.size(msg)[0] // 1.5, 70)

        back_width, back_height = font_options.size("Back")
        back_rect = pygame.Rect(screen_width//2 - back_width//1.5, 170, back_width, back_height)

        draw_text(msg, font_title, (255, 255, 255), back_rect, 0, 0)#screen_width//2 - back_width[0] // 1.5, 70)


