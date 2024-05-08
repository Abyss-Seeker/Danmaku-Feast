import pygame
import sys
import os
from pygame.locals import *
from config import *
import Boss_Fight_Challenge

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Initialize Pygame
screen_position = (screen_width - 100, screen_height // 2 - 380)
os.environ['SDL_VIDEO_WINDOW_POS'] = "{},{}".format(screen_position[0], screen_position[1])
pygame.init()

# Set up the window
screen_width = 600
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Starting Interface")

# Fonts
font_title = pygame.font.SysFont(None, 48)
font_subtitle = pygame.font.SysFont(None, 24)
font_options = pygame.font.SysFont(None, 36)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)  # Change to topleft alignment
    surface.blit(textobj, textrect)

def starting_interface():
    while True:
        screen.fill(BLACK)

        # Draw title and subtitle
        draw_text("Boss Fight Challenge", font_title, WHITE, screen, screen_width // 2 - font_options.size('Boss Fight Challenge')[0] // 1.5, 50)
        draw_text("ver. 0.1.0", font_subtitle, WHITE, screen, screen_width // 2 + 160, 80)

        # Get mouse position
        mouse_pos = pygame.mouse.get_pos()

        # Draw text with left alignment and color change when cursor is on it
        text_width_fight, text_height_fight = font_options.size('Fight')  # Get text width and height of Fight
        text_width_highscores, text_height_highscores = font_options.size('Highscores')  # Get text width and height
        text_fight_x = 425
        text_fight_y = 125
        text_highscores_x = 425
        text_highscores_y = 175

        # Adjust mouse detection area for more accuracy
        fight_rect = pygame.Rect(text_fight_x, text_fight_y, text_width_fight, text_height_fight)
        highscores_rect = pygame.Rect(text_highscores_x, text_highscores_y, text_width_highscores, text_height_highscores)

        if fight_rect.collidepoint(mouse_pos):
            draw_text('Fight', font_options, RED, screen, text_fight_x, text_fight_y)
        else:
            draw_text('Fight', font_options, WHITE, screen, text_fight_x, text_fight_y)

        if highscores_rect.collidepoint(mouse_pos):
            draw_text('Highscores', font_options, RED, screen, text_highscores_x, text_highscores_y)
        else:
            draw_text('Highscores', font_options, WHITE, screen, text_highscores_x, text_highscores_y)

        # Handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if fight_rect.collidepoint(mouse_pos):
                    return 'fight'
                elif highscores_rect.collidepoint(mouse_pos):
                    return 'highscores'

        pygame.display.update()

# Entry point
if __name__ == '__main__':
    option = starting_interface()
    if option == 'fight':
        Boss_Fight_Challenge.game(screen)
    elif option == 'highscores':
        # Handle highscores option
        pass
