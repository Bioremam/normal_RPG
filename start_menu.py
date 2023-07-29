from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import sys

pygame.init()
black = (0,0,0)
white = (255,255,255)
font = pygame.font.Font('ipaexg00401/ipaexg.ttf', 20)

def start_menu(bg):
    
    from dateclass import para
    point = 0
    
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    if point == 1:
                        point = 0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    if point == 0:
                        point = 1
        
        key = pygame.key.get_pressed()

        if key[pygame.K_f] == 1:
            if point == 0:
                    para.new_start()
                    break
            
            if point == 1:
                    para.__init__() #para.load_file()
                    break
        
        if point == 0:
            bg.fill(black)
            text = font.render('最初から', True,white)
            bg.blit(text,(300,200))
            text = font.render('続きから', True,white)
            bg.blit(text,(300,400))
            text = font.render('->', True,white)
            bg.blit(text,(200,200))
        else:
            bg.fill(black)
            text = font.render('最初から', True,white)
            bg.blit(text,(300,200))
            text = font.render('続きから', True,white)
            bg.blit(text,(300,400))
            text = font.render('->', True,white)
            bg.blit(text,(200,400))
        
        pygame.display.update()