import pygame
import sys
import os
from pygame.locals import *
from config import *
import Boss_Fight_Challenge
from Danmaku import danmaku_name
from Starting_GUI import draw_text, init_bullet_lists
from Starting_GUI import font_options, font_subtitle, font_title

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

name_lst = list(danmaku_name.keys())
name_lst.append("Back")
size_lst = []
pos_lst = []
rect_lst = []

idx = 0
for danmaku in name_lst:
    text_width, text_height = font_options.size(danmaku)
    x, y = 375, 125 + idx * 50
    rect = pygame.Rect(x, y, text_width, text_height)

    size_lst.append((text_width, text_height))
    pos_lst.append((x, y))
    rect_lst.append(rect)
    idx += 1



def game(screen):
    while True:
        screen.fill(BLACK)

        # Draw title and subtitle
        draw_text("Practice room", font_title, WHITE, screen, screen_width // 2 - font_options.size('Boss Fight Challenge')[0] // 1.5, 50)

        # Get mouse position
        mouse_pos = pygame.mouse.get_pos()
        

        for i in range(len(name_lst)):
            if rect_lst[i].collidepoint(mouse_pos):
                draw_text(name_lst[i], font_options, RED, screen, pos_lst[i][0], pos_lst[i][1])
            else:
                draw_text(name_lst[i], font_options, WHITE, screen, pos_lst[i][0], pos_lst[i][1])
            
        attack = -1

        # jasper我现在有点手痒想戳戳你的大腿的触感
        # Handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                for i in range(len(rect_lst)-1):
                    if rect_lst[i].collidepoint(mouse_pos):
                        attack = danmaku_name[name_lst[i]]
                # Return to menu
                if rect_lst[-1].collidepoint(mouse_pos):
                    return
                        
        if attack != -1:
            Boss_Fight_Challenge.game(screen, attack=attack)
            init_bullet_lists()

        pygame.display.set_caption("Practice room")
        pygame.display.update()

