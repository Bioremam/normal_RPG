from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import sys

pygame.init()
black = (0,0,0)
white = (255,255,255)
font = pygame.font.Font('ipaexg00401/ipaexg.ttf', 20)

def map0(bg):

    from dateclass import para

    while True:

        bg.fill(black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            
        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE] == 1:
            break
        
        text = font.render('上に移動: W', True,white)
        bg.blit(text,(100,100))
        text = font.render('下に移動: S', True,white)
        bg.blit(text,(100,200))
        text = font.render('左に移動: A', True,white)
        bg.blit(text,(100,300))
        text = font.render('右に移動: D', True,white)
        bg.blit(text,(100,400))
        text = font.render('決定: F', True,white)
        bg.blit(text,(400,100))
        text = font.render('メニューを開く、閉じる: TAB', True,white)
        bg.blit(text,(400,200))
        text = font.render('戻るには     SPACEキー     を押してください', True,white)
        bg.blit(text,(100,500))
        
        pygame.display.update()