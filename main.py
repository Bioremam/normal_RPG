from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import sys
import random
import time
from move_player import move_player
from map import map1


def main():
    pygame.init()
    pygame.display.set_caption("normal_dungeon")
    screen = pygame.display.set_mode((720,720))
    clock = pygame.time.Clock()
    
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        
        

        from dateclass import para
        map1(screen)
        move_player(para.pl_y,para.pl_x)

if __name__ == '__main__':
    main()