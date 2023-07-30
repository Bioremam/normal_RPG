from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import random
from battle import battle_scene

def move_player(y,x,bg): # 主人公の移動
    
    from dateclass import para
    
    key = pygame.key.get_pressed()

    if  key[pygame.K_w] == 1:
        para.direction = 0
        if para.mapdate[y-1][x] < 9:
            if not para.is_move:
                para.pl_y  -= 1

                para.is_move = True
                para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                d = random.randint(0,200)
                if d <= 10:
                    battle_scene(bg)
                #print(para.pl_y,para.pl_x)

    if  key[pygame.K_s] == 1:
        para.direction = 2
        if para.mapdate[y+1][x] < 9:
            if not para.is_move:
                para.pl_y += 1

                para.is_move = True
                para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                d = random.randint(0,200)
                if d <= 10:
                    battle_scene(bg)
                #print(para.pl_y,para.pl_x)

    if  key[pygame.K_a] == 1:
        para.direction = 3
        if para.mapdate[y][x-1] < 9:
            if not para.is_move:
                para.pl_x -= 1

                para.is_move = True
                para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                d = random.randint(0,200)
                if d <= 10:
                    battle_scene(bg)
                #print(para.pl_y,para.pl_x)

    if key[pygame.K_d] == 1:
        para.direction = 1
        if para.mapdate[y][x+1] < 9:
            if not para.is_move:
                para.pl_x += 1

                para.is_move = True
                para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                d = random.randint(0,200)
                if d <= 10:
                    battle_scene(bg)
                #print(para.pl_y,para.pl_x)
    
    if para.is_move and pygame.time.get_ticks() > para.move_delay:
        para.is_move = False