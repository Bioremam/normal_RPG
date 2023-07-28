from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import time
import sys

black = (0,0,0)
white = (255,255,255)

floor_map2 = pygame.image.load("image/floor_map2.png")
cea = pygame.image.load("image/cea_map2.png")
iwa = pygame.image.load("image/iwa.png")
cave = pygame.image.load("image/cave.png")
bridge_yoko = pygame.image.load("image/bridge_brown_yoko.png")
bridge_tate = pygame.image.load("image/bridge_brown.png")
yuusya_left = pygame.image.load("image/勇者左.png")
yuusya_right = pygame.image.load("image/勇者右.png")
yuusya_up = pygame.image.load("image/勇者上.png")
yuusya_down = pygame.image.load("image/勇者下.png")
castle = pygame.image.load("image/castle.png")

def map2(bg):
    bg.fill(black)

    from dateclass import para

    para.mapdate = []

    for h in range(54):
        para.mapdate.append([0]*74)

    '''0 = floor_map2
       1 = cave
       2 = 
       3 = bridge_yoko
       4 = bridge_tate
       5 = 
       9 = iwa
       10 = cea
       11 = 
       12 = 
       13 = 
       14 = 
       15 = '''
    


    for i in range(54):
        for j in range(74):
            if 0 <= i <= 11 or 42 <= i <= 53 or 0 <= j <= 11 or 62 <= j <= 73:
                para.mapdate[i][j] = 10
            if i == 12:
                if 12 <= j <= 28 or 32 <= j <= 61:
                    para.mapdate[i][j] = 9
                if 29 <= j <= 31:
                    para.mapdate[i][j] = 10
            elif i == 13:
                if 12 <= j <= 15 or 26 <= j <= 28 or 32 <= j <= 34 or 58 <= j <= 61:
                    para.mapdate[i][j] = 9
                if 29 <= j <= 31:
                    para.mapdate[i][j] = 10
            elif i == 14:
                if 12 <= j <= 14 or 26 <= j <= 28 or 32 <= j <= 33 or 59 <= j <= 61:
                    para.mapdate[i][j] = 9
                if 29 <= j <= 31:
                    para.mapdate[i][j] = 10
            elif i == 15:
                if 12 <= j <= 14 or j == 28 or 30 <= j <= 32 or 60 <= j <= 61:
                    para.mapdate[i][j] = 9
                if j == 29:
                    para.mapdate[i][j] = 10
            elif i == 16:
                if j == 12 or 27 <= j <= 28 or j == 30 or j == 61:
                    para.mapdate[i][j] = 9
                if j == 29:
                    para.mapdate[i][j] = 10
            elif i == 17:
                if j == 12 or j == 27 or j == 30 or j == 61:
                    para.mapdate[i][j] = 9
                if 28 <= j <= 29:
                    para.mapdate[i][j] = 10
                if j == 16:
                    para.mapdate[i][j] = 1
            elif i == 18:
                if j == 12 or j == 27 or j == 30 or j == 61:
                    para.mapdate[i][j] = 9
                if 28 <= j <= 29:
                    para.mapdate[i][j] = 10 
            elif i == 19:
                if j == 12 or j == 26 or 29 <= j <= 30 or j == 61:
                    para.mapdate[i][j] = 9
                if 27 <= j <= 28:
                    para.mapdate[i][j] = 10
            elif i == 20:
                if j == 12 or j == 61:
                    para.mapdate[i][j] = 9
                if 27 <= j <= 28:
                    para.mapdate[i][j] = 3
                if j == 53:
                    para.mapdate[20][53] = 5
            elif i == 21:
                if j == 12 or j == 26 or j == 29 or j == 61:
                    para.mapdate[i][j] = 9
                if 27 <= j <= 28:
                    para.mapdate[i][j] = 10
            elif i == 22:
                if j == 12 or j == 26 or 28 <= j <= 29 or j == 61:
                    para.mapdate[i][j] = 9
                if j == 27:
                    para.mapdate[i][j] = 10
            elif i == 23:
                if j == 12 or j == 26 or j == 28 or j == 61:
                    para.mapdate[i][j] = 9
                if j == 27:
                    para.mapdate[i][j] = 10
            elif i == 24:
                if j == 12 or 25 <= j <= 26 or j == 28 or j == 61:
                    para.mapdate[i][j] = 9
                if j == 27:
                    para.mapdate[i][j] = 10
            elif i == 25:
                if j == 12 or j == 25 or 28 <= j <= 29 or j == 61:
                    para.mapdate[i][j] = 9
                if 26 <= j <= 27:
                    para.mapdate[i][j] = 10
            elif i == 26:
                if j == 12 or j == 25 or 28 <= j <= 30 or 33 <= j <= 34 or j == 61:
                    para.mapdate[i][j] = 9
                if 26 <= j <= 27:
                    para.mapdate[i][j] = 10
            elif i == 27:
                if j == 12 or 24 <= j <= 25 or 30 <= j <= 35 or j == 61:
                    para.mapdate[i][j] = 9
                if 26 <= j <= 29:
                    para.mapdate[i][j] = 10
            elif i == 28:
                if j == 12 or j == 23 or 35 <= j <= 40 or 50 <= j <= 53 or j == 61:
                    para.mapdate[i][j] = 9
                if 24 <= j <= 34:
                    para.mapdate[i][j] = 10
            elif i == 29:
                if j == 12 or 22 <= j <= 23 or 27 <= j <= 29 or j == 40 or 49 <= j <= 50 or 53 <= j <= 55 or 60 <= j <= 61:
                    para.mapdate[i][j] = 9
                if 24 <= j <= 26 or 30 <= j <= 39 or 51 <= j <= 52:
                    para.mapdate[i][j] = 10
            elif i == 30:
                if j == 12 or 21 <= j <= 22 or j == 27 or 29 <= j <= 30 or 40 <= j <= 45 or 47 <= j <= 49 or 55 <= j <= 61:
                    para.mapdate[i][j] = 9
                if 23 <= j <= 26 or 31 <= j <= 39 or 50 <= j <= 54:
                    para.mapdate[i][j] = 10
            elif i == 31:
                if j == 12 or 20 <= j <= 21 or 24 <= j <= 27 or 30 <= j <= 34 or 52 <= j<= 53:
                    para.mapdate[i][j] = 9
                if 22 <= j <= 23 or 34 <= j <= 45 or 47 <= j <= 51 or 54 <= j <= 61:
                    para.mapdate[i][j] = 10
                if j == 46:
                    para.mapdate[i][j] = 4
            elif i == 32:
                if j == 12 or 18 <= j <= 20 or 23 <= j <= 24 or 33 <= j <= 39 or 50 <= j<= 58:
                    para.mapdate[i][j] = 9
                if 21 <= j <= 22 or 40 <= j <= 45 or 47 <= j <= 49 or 59 <= j <= 61:
                    para.mapdate[i][j] = 10
                if j == 46:
                    para.mapdate[i][j] = 4
            elif i == 33:
                if j == 12 or 17 <= j <= 18 or 22 <= j <= 23 or 39 <= j <= 45 or 47 <= j<= 50 or 55 <= j <= 61:
                    para.mapdate[i][j] = 9
                if 19 <= j <= 21:
                    para.mapdate[i][j] = 10
            elif i == 34:
                if j == 12 or j == 17 or j == 22 or j == 61:
                    para.mapdate[i][j] = 9
                if 18 <= j <= 21:
                    para.mapdate[i][j] = 10
            elif i == 35:
                if j == 12 or j == 17 or 20 <= j <= 22 or j == 61:
                    para.mapdate[i][j] = 9
                if 18 <= j <= 19:
                    para.mapdate[i][j] = 10
            elif i == 36:
                if j == 12 or j == 17 or 19 <= j <= 20 or j == 61:
                    para.mapdate[i][j] = 9
                if j == 18:
                    para.mapdate[i][j] = 10
            elif i == 37:
                if j == 12 or j == 17 or j == 19 or j == 61:
                    para.mapdate[i][j] = 9
                if j == 18:
                    para.mapdate[i][j] = 10
            elif i == 38:
                if j == 12 or j == 61:
                    para.mapdate[i][j] = 9
                if j == 18:
                    para.mapdate[i][j] = 3
            elif i == 39:
                if j == 12 or 16 <= j <= 17 or 19 <= j <= 20 or j == 61:
                    para.mapdate[i][j] = 9
                if j == 18:
                    para.mapdate[i][j] = 10
            elif i == 40:
                if 12 <= j <= 13 or 15 <= j <= 16 or 19 <= j <= 21 or j == 61:
                    para.mapdate[i][j] = 9
                if 17 <= j <= 18:
                    para.mapdate[i][j] = 10
            elif i == 41:
                if 12 <= j <= 16 or 18 <= j <= 61:
                    para.mapdate[i][j] = 9
                if j == 17:
                    para.mapdate[i][j] = 10

    
def back_map2(bg):
    bg.fill(black)

    from dateclass import para    


    for y in range(-12,12):
        for x in range(-12,12):
            X,Y = (x+12)*30,(y+12)*30
            dx,dy = para.pl_x+x,para.pl_y+y
            if 0 <= dx < 73 and 0 <= dy < 53:
                if para.mapdate[dy][dx] == 0:
                    bg.blit(floor_map2,[X,Y])
                if para.mapdate[dy][dx] == 1:
                    bg.blit(cave,[X,Y])
                if para.mapdate[dy][dx] == 3:
                    bg.blit(bridge_yoko,[X,Y])
                if para.mapdate[dy][dx] == 4:
                    bg.blit(bridge_tate,[X,Y])
                if para.mapdate[dy][dx] == 5:
                    bg.blit(castle,[X,Y])
                if para.mapdate[dy][dx] == 9:
                    bg.blit(iwa,[X,Y])
                if para.mapdate[dy][dx] == 10:
                    bg.blit(cea,[X,Y])
                if x == 0 and y == 0:
                    if para.mapdate[dy][dx] < 9:
                        if para.direction == 0:
                            bg.blit(yuusya_up,[X,Y])
                        if para.direction == 1:
                            bg.blit(yuusya_right,[X,Y])
                        if para.direction == 2:
                            bg.blit(yuusya_down,[X,Y])
                        elif para.direction == 3:
                            bg.blit(yuusya_left,[X,Y])
    
    pygame.display.update()