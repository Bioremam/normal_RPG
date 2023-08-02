from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import sys

pygame.init()
black = (0,0,0)
white = (255,255,255)
font = pygame.font.Font('ipaexg00401/ipaexg.ttf', 20)
from map0 import map0

def start_menu(bg):
    
    from dateclass import para
    point = 1
    
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    if point > 0:
                        point -= 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    if point < 2:
                        point += 1
        
        key = pygame.key.get_pressed()

        if key[pygame.K_f] == 1:
            if point == 0:
                    para.new_start()
                    break
            if point == 1:
                    para.__init__() #para.load_file()
                    break
            if point == 2:
                    map0(bg)

        bg.fill(black)
        text = font.render('最初から', True,white)
        bg.blit(text,(300,180))
        text = font.render('続きから', True,white)
        bg.blit(text,(300,380))
        text = font.render('操作方法', True,white)
        bg.blit(text,(300,580))
        
        if point == 0:
            text = font.render('->', True,white)
            bg.blit(text,(200,180))
        elif point == 1:
            text = font.render('->', True,white)
            bg.blit(text,(200,380))
        else:
            text = font.render('->', True,white)
            bg.blit(text,(200,580))
             
        pygame.display.update()