from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import time
import sys

pygame.init()
black = (0,0,0)
white = (255,255,255)
font = pygame.font.Font('ipaexg00401/ipaexg.ttf', 20)

hana = pygame.image.load("image/maptile_sogen_hana.png")
floor = pygame.image.load("image/floor.png")
desk = pygame.image.load("image/floor_desk.png")
cea = pygame.image.load("image/cea.png")
wall = pygame.image.load("image/wall.png")
bridge_tate = pygame.image.load("image/bridge_brown.png")
bridge_yoko = pygame.image.load("image/bridge_brown_yoko.png")
yuusya_left = pygame.image.load("image/勇者左.png")
yuusya_right = pygame.image.load("image/勇者右.png")
yuusya_up = pygame.image.load("image/勇者上.png")
yuusya_down = pygame.image.load("image/勇者下.png")
door_left = pygame.image.load("image/門左.png")
door_right = pygame.image.load("image/門右.png")
merchant01 = pygame.image.load("image/merchant01.png")
merchant02 = pygame.image.load("image/merchant02.png")
hotelman = pygame.image.load("image/hotelman.png")
client = pygame.image.load("image/client.png")

def map1(bg):
    bg.fill(black)

    from dateclass import para

    for h in range(32):
        for w in range(32):
            para.mapdate[h][w] = 0
    
    '''0 = hana
       1 = door_left
       2 = door_right
       3 = bridge_yoko
       4 = bridge_tate
       5 = floor
       9 = wall
       10 = cea
       11 = desk
       12 = merchant01
       13 = merchant02
       14 = hotelman
       15 = client  '''
    
    for i in range(31):
        for j in range(31):
            #外壁
            if i == 0 or i == 30 or j == 0 or j == 30:
                para.mapdate[i][j] = 9
            #中央壁
            if i == 6:
                if 8 <= j <= 22:
                    para.mapdate[i][j] = 9
            if i == 15:
                if 8 <= j <= 13 or 17 <= j <= 22:
                    para.mapdate[i][j] = 9
                #中央入口
                elif 14 <= j <= 16:
                    para.mapdate[i][j] = 5
            if 7 <= i <= 14:
                if j == 8 or j == 22:
                    para.mapdate[i][j] = 9
            if i == 21 or i == 27:
                if 4 <= j <= 11 or 19 <= j <= 26:
                    para.mapdate[i][j] = 9
            #中央床
            if 7 <= i <= 8 or 10 <= i <= 14:
                if 9 <= j <= 21:
                    para.mapdate[i][j] = 5
            #中央机
            if i == 9 and 9 <= j <= 21:
                para.mapdate[i][j] = 11

            para.mapdate[8][15] = 15
            #下建物二つ
            if 22 <= i <= 26:
                if j == 4 or j == 11 or j == 19 or j == 26:
                    para.mapdate[i][j] = 9
                if j == 5 or 7 <= j <= 10 or 20 <= j <= 23 or j == 25:
                    para.mapdate[i][j] = 5
                if j == 6 or j == 24:
                    para.mapdate[i][j] = 11
            para.mapdate[24][11] = 5
            para.mapdate[25][11] = 5
            para.mapdate[24][19] = 5
            para.mapdate[25][19] = 5
            para.mapdate[23][5] = 12
            para.mapdate[25][5] = 13
            para.mapdate[24][25] = 14
            
            #水堀
            if (3 <= i <= 4 and 4 <= j <= 26) or (17 <= i <= 18 and 4 <= j <= 26):
                para.mapdate[i][j] = 10
            if (3 <= i <= 18 and 4 <= j <= 5) or (3 <= i <= 18 and 25 <= j <= 26):
                para.mapdate[i][j] = 10
            if i == 10:
                #左右抜け道
                if j == 0 or j == 30:
                    para.mapdate[i][j] = 0
                #水堀橋横
                if (4 <= j <= 5) or (25 <= j <= 26):
                    para.mapdate[i][j] = 3
            #水堀橋縦
            if i == 17 or i == 18:
                if 14 <=  j <= 16:
                    para.mapdate[i][j] = 4
    #正面門
    para.mapdate[30][14],para.mapdate[30][15] = 1,2
            

    for y in range(-12,12):
        for x in range(-12,12):
            X,Y = (x+12)*30,(y+12)*30
            dx,dy = para.pl_x+x,para.pl_y+y
            if 0 <= dx < 31 and 0 <= dy < 31:
                if para.mapdate[dy][dx] == 0:
                    bg.blit(hana,[X,Y])
                if para.mapdate[dy][dx] == 9:
                    bg.blit(wall,[X,Y])
                if para.mapdate[dy][dx] == 10:
                    bg.blit(cea,[X,Y])    
                if para.mapdate[dy][dx] == 11:
                    bg.blit(desk,[X,Y])
                if para.mapdate[dy][dx] == 12:
                    bg.blit(merchant01,[X,Y])
                if para.mapdate[dy][dx] == 13:
                    bg.blit(merchant02,[X,Y])
                if para.mapdate[dy][dx] == 14:
                    bg.blit(hotelman,[X,Y])
                if para.mapdate[dy][dx] == 15:
                    bg.blit(client,[X,Y])                           
                if para.mapdate[dy][dx] == 1:
                    bg.blit(door_left,[X,Y])
                if para.mapdate[dy][dx] == 2:
                    bg.blit(door_right,[X,Y])
                if para.mapdate[dy][dx] == 3:
                    bg.blit(bridge_yoko,[X,Y])
                if para.mapdate[dy][dx] == 4:
                    bg.blit(bridge_tate,[X,Y])
                if para.mapdate[dy][dx] == 5:
                    bg.blit(floor,[X,Y])
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
    if para.pl_y == 23 and para.pl_x == 7 and para.direction == 3:
        
        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE] == 1:
            talk_merchant01(bg)

    if para.pl_y == 25 and para.pl_x == 7 and para.direction == 3:
        
        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE] == 1:
            talk_merchant02(bg)

    if para.pl_y == 24 and para.pl_x == 23 and para.direction == 1:
        
        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE] == 1:
            talk_hotelman(bg)
        
    pygame.display.update()

def talk_merchant01(bg):
        
        from dateclass import para
        point = 0
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        if point >= 1:
                            point -= 1

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_s:
                        if point < 11:
                            point += 1       
            
            key = pygame.key.get_pressed()

            if key[pygame.K_e] == 1:
                if point == 11:
                    break
            
            #pygame.draw.rect(bg,black,(0,40,300,300),border_radius = 5)
            bg.fill(black,(0,40,300,290))
            pygame.draw.rect(bg,white,(0,40,300,290),width = 5,border_radius = 5)
            text = font.render('    薬草       5 G', True,white)
            bg.blit(text,(5,50))
            text = font.render('    魔法草     8 G', True,white)
            bg.blit(text,(5,73))
            text = font.render('買い物を終了する', True,white)
            bg.blit(text,(5,302))
            now = 49+point*23
            pygame.draw.rect(bg,white,(5,now,290,23),width = 1,border_radius = 5)           

            pygame.display.update()

def talk_merchant02(bg):
        
        from dateclass import para
        point = 0
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        if point >= 1:
                            point -= 1

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_s:
                        if point < 11:
                            point += 1       
            
            key = pygame.key.get_pressed()

            if key[pygame.K_e] == 1:
                if point == 11:
                    break
            
            #pygame.draw.rect(bg,black,(0,40,300,300),border_radius = 5)
            bg.fill(black,(0,40,300,290))
            pygame.draw.rect(bg,white,(0,40,300,290),width = 5,border_radius = 5)
            text = font.render('    木刀     10 G', True,white)
            bg.blit(text,(5,50))
            text = font.render('    鋼の剣     15 G', True,white)
            bg.blit(text,(5,73))
            text = font.render('    木の盾     10 G', True,white)
            bg.blit(text,(5,96))
            text = font.render('    銅の盾     15 G', True,white)
            bg.blit(text,(5,119))
            text = font.render('買い物を終了する', True,white)
            bg.blit(text,(5,302))
            now = 49+point*23
            pygame.draw.rect(bg,white,(5,now,290,23),width = 1,border_radius = 5)           

            pygame.display.update()

def talk_hotelman(bg):
        
        from dateclass import para
        point = 0
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        if point >= 1:
                            point -= 1

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_s:
                        if point < 1:
                            point += 1       
            
            key = pygame.key.get_pressed()

            if key[pygame.K_e] == 1:
                if point == 1:
                    break
            
            #pygame.draw.rect(bg,black,(0,40,300,300),border_radius = 5)
            bg.fill(black,(0,40,300,62))
            pygame.draw.rect(bg,white,(0,40,300,62),width = 5,border_radius = 5)
            text = font.render('泊まっていく', True,white)
            bg.blit(text,(5,50))
            text = font.render('やめる', True,white)
            bg.blit(text,(5,73))
            now = 49+point*23
            pygame.draw.rect(bg,white,(5,now,290,23),width = 1,border_radius = 5)           

            pygame.display.update()