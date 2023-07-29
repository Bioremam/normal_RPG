from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import time
import sys

pygame.init()
black = (0,0,0)
white = (255,255,255)
yellow = (255,248,64)
font = pygame.font.Font('ipaexg00401/ipaexg.ttf', 20)

hana = pygame.image.load("image/maptile_sogen_hana.png")
floor = pygame.image.load("image/floor.png")
desk = pygame.image.load("image/floor_desk.png")
cea = pygame.image.load("image/cea_map1.png")
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

    para.mapdate = []

    for i in range(32):
        para.mapdate.append([0]*32)

    '''for h in range(32):
        for w in range(32):
            para.mapdate[h][w] = 0'''
    
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
    para.mapdate[30][14],para.mapdate[30][15],para.mapdate[30][16] = 1,2,2
            
def back_map1(bg):

    bg.fill(black)

    from dateclass import para    

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
    
    key = pygame.key.get_pressed()

    if para.pl_y == 23 and para.pl_x == 7 and para.direction == 3:

        if key[pygame.K_f] == 1:
            if not para.is_move:
                para.is_move = True
                para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                talk_merchant01(bg)

    if para.pl_y == 25 and para.pl_x == 7 and para.direction == 3:

        if key[pygame.K_f] == 1:
            if not para.is_move:
                para.is_move = True
                para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                talk_merchant02(bg)

    if para.pl_y == 24 and para.pl_x == 23 and para.direction == 1:

        if key[pygame.K_f] == 1:
            if not para.is_move:
                para.is_move = True
                para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                talk_hotelman(bg)
    
    if para.pl_y == 10 and para.pl_x == 15 and para.direction == 0:

        if key[pygame.K_f] == 1:
            if not para.is_move:
                para.is_move = True
                para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                talk_client(bg)

    if para.is_move and pygame.time.get_ticks() > para.move_delay:
        para.is_move = False
        
    pygame.display.update()

def talk_merchant01(bg):
        
    from dateclass import para
    point = 0
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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

        if key[pygame.K_f] == 1:
            if point == 11:
                if not para.is_move:
                    para.is_move = True
                    para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                    break
            
            if point == 0:
                if not para.is_move:
                    if para.money >= 5:
                        para.is_move = True
                        para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                        para.bag_item["薬草"] += 1
                        para.money -= 5

            if point == 1:
                if not para.is_move:
                    if para.money >= 8:
                        para.is_move = True
                        para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                        para.bag_item["魔法草"] += 1
                        para.money -= 8

        if key[pygame.K_ESCAPE] == 1:
            if not para.is_move:
                para.is_move = True
                para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                break

        if para.is_move and pygame.time.get_ticks() > para.move_delay:
            para.is_move = False
        
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

        draw_status(bg)

        pygame.display.update()

def talk_merchant02(bg):
        
    from dateclass import para
    point = 0
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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

        if key[pygame.K_f] == 1:
            if point == 11:
                if not para.is_move:
                    para.is_move = True
                    para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                    break

            if point == 0:
                if not para.is_move:
                    if para.money >= 10:
                        para.is_move = True
                        para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                        para.bag_equip["木刀"] += 1
                        para.equip_status["木刀"][0] = 0
                        para.equip_status["木刀"][1] = 5
                        para.money -= 10

            if point == 1:
                if not para.is_move:
                    if para.money >= 15:
                        para.is_move = True
                        para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                        para.bag_equip["鋼の剣"] += 1
                        para.equip_status["鋼の剣"][0] = 0
                        para.equip_status["鋼の剣"][1] = 10
                        para.money -= 15

            if point == 2:
                if not para.is_move:
                    if para.money >= 10:
                        para.is_move = True
                        para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                        para.bag_equip["木の盾"] += 1
                        para.equip_status["木の盾"][0] = 1
                        para.equip_status["木の盾"][1] = 5
                        para.money -= 10

            if point == 3:
                if not para.is_move:
                    if para.money >= 15:
                        para.is_move = True
                        para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                        para.bag_equip["銅の盾"] += 1
                        para.equip_status["銅の盾"][0] = 1
                        para.equip_status["銅の盾"][1] = 10
                        para.money -= 15
        
        if key[pygame.K_ESCAPE] == 1:
            if not para.is_move:
                para.is_move = True
                para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                break

        if para.is_move and pygame.time.get_ticks() > para.move_delay:
            para.is_move = False
        
        draw_status(bg)
        
        #pygame.draw.rect(bg,black,(0,40,300,300),border_radius = 5)
        bg.fill(black,(0,40,300,290))
        pygame.draw.rect(bg,white,(0,40,300,290),width = 5,border_radius = 5)
        text = font.render('    木刀     10 G', True,white)
        bg.blit(text,(5,50))
        if point == 0:
            text = font.render("+ 5",True,yellow)
            bg.blit(text,(180,410))
        text = font.render('    鋼の剣     15 G', True,white)
        bg.blit(text,(5,73))
        if point == 1:
            text = font.render("+ 10",True,yellow)
            bg.blit(text,(180,410))
        text = font.render('    木の盾     10 G', True,white)
        bg.blit(text,(5,96))
        if point == 2:
            text = font.render("+ 5",True,yellow)
            bg.blit(text,(180,450))
        text = font.render('    銅の盾     15 G', True,white)
        bg.blit(text,(5,119))
        if point == 3:
            text = font.render("+ 10",True,yellow)
            bg.blit(text,(180,450))
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
                if not para.is_move:
                    para.is_move = True
                    para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                    para.hp = para.max_hp
                    para.mp = para.max_mp
                    para.money -= 10
                    break

        if key[pygame.K_f] == 1:
            if point == 1:
                if not para.is_move:
                    para.is_move = True
                    para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                    break

        if key[pygame.K_ESCAPE] == 1:
            if not para.is_move:
                para.is_move = True
                para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                break

        if para.is_move and pygame.time.get_ticks() > para.move_delay:
            para.is_move = False
        
        #pygame.draw.rect(bg,black,(0,40,300,300),border_radius = 5)
        bg.fill(black,(0,40,300,62))
        pygame.draw.rect(bg,white,(0,40,300,62),width = 5,border_radius = 5)
        text = font.render('泊まっていく  10 G', True,white)
        bg.blit(text,(5,50))
        text = font.render('やめる', True,white)
        bg.blit(text,(5,73))
        now = 49+point*23
        pygame.draw.rect(bg,white,(5,now,290,23),width = 1,border_radius = 5)           

        draw_status(bg)

        pygame.display.update()

def talk_client(bg):
    
    from dateclass import para
    point = 0
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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

        if key[pygame.K_f] == 1:
            if point == 11:
                if not para.is_move:
                    para.is_move = True
                    para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                    break

        if key[pygame.K_ESCAPE] == 1:
            if not para.is_move:
                para.is_move = True
                para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                break

        if para.is_move and pygame.time.get_ticks() > para.move_delay:
            para.is_move = False
        
        #pygame.draw.rect(bg,black,(0,40,300,300),border_radius = 5)
        bg.fill(black,(0,40,300,290))
        pygame.draw.rect(bg,white,(0,40,300,290),width = 5,border_radius = 5)
        text = font.render('クエスト No1', True,white)
        bg.blit(text,(5,50))
        text = font.render('クエスト No2', True,white)
        bg.blit(text,(5,73))
        text = font.render('クエスト No3', True,white)
        bg.blit(text,(5,96))
        text = font.render('やめる', True,white)
        bg.blit(text,(5,302))
        now = 49+point*23
        pygame.draw.rect(bg,white,(5,now,290,23),width = 1,border_radius = 5)

        draw_status(bg)

        pygame.display.update()

def draw_status(bg):
        
        from dateclass import para

        #メニュー　ステータス
        bg.fill(black,(0,330,300,290))
        pygame.draw.rect(bg,white,(0,330,300,290),width = 5,border_radius = 5)
        
        #hp
        pygame.draw.rect(bg,(255,138,197),(20,350,100,10)) #ピンク
        nowhp_rate = (para.hp/para.max_hp)*100
        pygame.draw.rect(bg,(0,208,0),(20,350,nowhp_rate,10)) #緑
        text = font.render("HP  {} / {}".format(para.hp,para.max_hp),True,white)
        bg.blit(text,(150,347))
        
        #mp
        pygame.draw.rect(bg,(142,219,255),(20,380,100,10)) #水色
        nowmp_rate = (para.mp/para.max_mp)*100
        pygame.draw.rect(bg,(5,69,255),(20,380,nowmp_rate,10)) #青色
        text = font.render("MP  {} / {}".format(para.mp,para.max_mp),True,white)
        bg.blit(text,(150,377))

        #攻撃力
        text = font.render("攻撃力  {}".format(para.attack),True,white)
        bg.blit(text,(50,410))

        #防御力
        text = font.render("防御力  {}".format(para.deffence),True,white)
        bg.blit(text,(50,450))

        #所持金
        text = font.render("所持金  {} G".format(para.money),True,white)
        bg.blit(text,(50,490))