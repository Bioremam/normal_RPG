from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import sys
import random
import time
from move_player import move_player
from map1 import map1,back_map1
from map2 import map2,back_map2
from msg import menu,exit_town,enter_town


def main():
    pygame.init()
    pygame.display.set_caption("normal_dungeon")
    screen = pygame.display.set_mode((720,720))
    clock = pygame.time.Clock()
    from dateclass import para
    
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        if para.map == 10:
            map1(screen)
            para.map = 11
        elif para.map == 11:
            back_map1(screen)
            if para.pl_y == 30:
                if para.pl_x == 14 or para.pl_x == 15 or para.pl_x == 16:
                    exit_town(screen)
        
        elif para.map == 20:
            map2(screen)
            para.map = 21
        elif para.map == 21:
            back_map2(screen)
            if para.pl_y == 20:
                if para.pl_x == 53:
                    enter_town(screen)
        
        key = pygame.key.get_pressed()

        if key[pygame.K_TAB] == 1:
            if not para.is_move:
                para.is_move = True
                para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                menu(screen)

        if para.is_move and pygame.time.get_ticks() > para.move_delay:
            para.is_move = False

        move_player(para.pl_y,para.pl_x)
        clock.tick(30)
        
if __name__ == '__main__':
    main()