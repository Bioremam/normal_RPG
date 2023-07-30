from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import sys
import time

pygame.init()
black = (0,0,0)
white = (255,255,255)
font = pygame.font.Font('ipaexg00401/ipaexg.ttf', 20)
clock = pygame.time.Clock()

def menu(bg):

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

        if point == 0:
            show_item(bg)
            if key[pygame.K_f] == 1:
                if not para.is_move:
                    if len(para.bag_item) != 0:
                        para.is_move = True
                        para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                        item(bg)
        if point == 1:
            show_equip(bg)
            if key[pygame.K_f] == 1:
                if not para.is_move:
                    if len(para.bag_equip) != 0:
                        para.is_move = True
                        para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                        equip(bg)
        if point == 2:
            show_save(bg)
            if key[pygame.K_f] == 1:
                if not para.is_move:
                    para.is_move = True
                    para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                    text = font.render('セーブが完了しました', True,white)
                    bg.blit(text,(305,50))
                    pygame.display.update()
                    time.sleep(1)
                    para.savefile()
                    break
        elif point == 11:
            if key[pygame.K_f] == 1:
                if not para.is_move:
                    para.is_move = True
                    para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                    break
        
        if key[pygame.K_TAB] == 1:
            if not para.is_move:
                para.is_move = True
                para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                break

        if para.is_move and pygame.time.get_ticks() > para.move_delay:
            para.is_move = False
        
        #pygame.draw.rect(bg,black,(0,40,300,300),border_radius = 5)
        bg.fill(black,(0,40,300,290))
        pygame.draw.rect(bg,white,(0,40,300,290),width = 5,border_radius = 5)
        text = font.render('     道具', True,white)
        bg.blit(text,(5,50))
        text = font.render('     装備', True,white)
        bg.blit(text,(5,73))
        text = font.render('     セーブする', True,white)
        bg.blit(text,(5,96))
        text = font.render('     閉じる', True,white)
        bg.blit(text,(5,302))
        now = 49+point*23
        pygame.draw.rect(bg,white,(5,now,290,23),width = 1,border_radius = 5)           

        draw_status(bg)

        clock.tick(30)
        pygame.display.update()

def show_item(bg):
        
        bg.fill(black,(300,40,300,290))
        pygame.draw.rect(bg,white,(300,40,300,290),width = 5,border_radius = 5)
        draw_bag_item(bg)
        '''text = font.render('     所持品1', True,white)
        bg.blit(text,(305,50))
        text = font.render('     所持品2', True,white)
        bg.blit(text,(305,73))
        text = font.render('     閉じる', True,white)
        bg.blit(text,(305,302))'''       

        pygame.display.update()

def show_equip(bg):
        
        bg.fill(black,(300,40,300,290))
        pygame.draw.rect(bg,white,(300,40,300,290),width = 5,border_radius = 5)
        draw_bag_equip(bg)
        '''text = font.render('     装備1', True,white)
        bg.blit(text,(305,50))
        text = font.render('     装備2', True,white)
        bg.blit(text,(305,73))
        text = font.render('     閉じる', True,white)
        bg.blit(text,(305,302))'''          

        pygame.display.update()

def show_save(bg):

        bg.fill(black,(300,40,300,290))
        pygame.draw.rect(bg,white,(300,40,300,290),width = 5,border_radius = 5)
        pygame.display.update()

def item(bg):
    
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
            if not para.is_move:
                if point == 11:
                    para.is_move = True
                    para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                    pygame.display.update()
                    break
                
                if point == 0:
                    para.is_move = True
                    para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                    use_item(bg,point)
                
                if point == 1:
                    para.is_move = True
                    para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                    use_item(bg,point)

        if key[pygame.K_ESCAPE] == 1:
            if not para.is_move:
                para.is_move = True
                para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                break

        if para.is_move and pygame.time.get_ticks() > para.move_delay:
            para.is_move = False

        
        #pygame.draw.rect(bg,black,(0,40,300,300),border_radius = 5)
        bg.fill(black,(300,40,300,290))
        pygame.draw.rect(bg,white,(300,40,300,290),width = 5,border_radius = 5)

        draw_bag_item(bg)
        '''text = font.render('     薬草{}'.format(para.bag["薬草"]),True,white)
        bg.blit(text,(305,50))
        text = font.render('     魔法草',True,white)
        bg.blit(text,(305,73))
        text = font.render('     閉じる',True,white)
        bg.blit(text,(305,302))'''
        now = 49+point*23
        pygame.draw.rect(bg,white,(305,now,290,23),width = 1,border_radius = 5)

        pygame.display.update()

def equip(bg):

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
            if not para.is_move:
                if point == 11:
                    para.is_move = True
                    para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                    pygame.display.update()
                    break
                if point == 0:
                    para.is_move = True
                    para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                    use_equip(bg,point)
                if point == 1:
                    para.is_move = True
                    para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                    use_equip(bg,point)
                if point == 2:
                    para.is_move = True
                    para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                    use_equip(bg,point)
                if point == 3:
                    para.is_move = True
                    para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                    use_equip(bg,point)

        if key[pygame.K_ESCAPE] == 1:
            if not para.is_move:
                para.is_move = True
                para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                break

        if para.is_move and pygame.time.get_ticks() > para.move_delay:
            para.is_move = False

        
        #pygame.draw.rect(bg,black,(0,40,300,300),border_radius = 5)
        bg.fill(black,(300,40,300,290))
        pygame.draw.rect(bg,white,(300,40,300,290),width = 5,border_radius = 5)
        draw_bag_equip(bg)
        '''text = font.render('     装備1', True,white)
        bg.blit(text,(305,50))
        text = font.render('     装備2', True,white)
        bg.blit(text,(305,73))
        text = font.render('     閉じる', True,white)
        bg.blit(text,(305,302))'''
        now = 49+point*23
        pygame.draw.rect(bg,white,(305,now,290,23),width = 1,border_radius = 5)

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

        text = font.render("Lv.   {}".format(para.lv),True,white)
        bg.blit(text,(50,530))

def exit_town(bg):

    from dateclass import para
    point = 1
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    if point >= 2:
                        point -= 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    if point < 2:
                        point += 1       
        
        key = pygame.key.get_pressed()

        if key[pygame.K_f] == 1:
            if point == 1:
                para.pl_y,para.pl_x = 21,53
                para.map = 20
                break
            else:
                para.pl_y -= 1
                break

        bg.fill(black,(0,40,300,85))
        pygame.draw.rect(bg,white,(0,40,300,85),width = 5,border_radius = 5)
        text = font.render('     町から出ますか？', True,white)
        bg.blit(text,(5,50))
        text = font.render('     出る', True,white)
        bg.blit(text,(5,73))
        text = font.render('     やっぱりやめる', True,white)
        bg.blit(text,(5,96))
        now = 49+point*23
        pygame.draw.rect(bg,white,(5,now,290,23),width = 1,border_radius = 5)           

        pygame.display.update()

def enter_town(bg):

    from dateclass import para
    point = 1
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    if point >= 2:
                        point -= 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    if point < 2:
                        point += 1       
        
        key = pygame.key.get_pressed()

        if key[pygame.K_f] == 1:
            if point == 1:
                para.pl_y,para.pl_x = 29,15
                para.map = 10
                break
            else:
                para.pl_y += 1
                break

        bg.fill(black,(0,40,300,85))
        pygame.draw.rect(bg,white,(0,40,300,85),width = 5,border_radius = 5)
        text = font.render('     町へ戻りますか？', True,white)
        bg.blit(text,(5,50))
        text = font.render('     戻る', True,white)
        bg.blit(text,(5,73))
        text = font.render('     やっぱりやめる', True,white)
        bg.blit(text,(5,96))
        now = 49+point*23
        pygame.draw.rect(bg,white,(5,now,290,23),width = 1,border_radius = 5)           

        pygame.display.update()

def draw_bag_item(bg):
    
    from dateclass import para
    point = 0

    for key in para.bag_item.keys():
        text = font.render('{}               {} 個'.format(key,para.bag_item[key]),True,white)
        bg.blit(text,(305,50+point*23))
        point += 1

def draw_bag_equip(bg):
    
    from dateclass import para
    point = 0

    for key in para.bag_equip.keys():
        text = font.render('{}               {} 個'.format(key,para.bag_equip[key]),True,white)
        bg.blit(text,(305,50+point*23))
        point += 1

def use_yakusou(bg):

    from dateclass import para

    if para.bag_item["薬草"] > 0:
        if para.hp + 5 <= para.max_hp:
            para.hp += 5
        else:
            para.hp = para.max_hp
        para.bag_item["薬草"] -= 1

def use_mahousou(bg):

    from dateclass import para

    if para.bag_item["魔法草"] > 0:
        if para.mp + 5 <= para.max_mp:
            para.mp += 5
        else:
            para.mp = para.max_mp
        para.bag_item["魔法草"] -= 1

def use_item(bg,point):

    check = 0

    from dateclass import para

    for i in list(para.bag_item.keys()):
        if check == point:
            if i == "薬草":
                if para.bag_item[i] >= 1:
                    if para.hp + 10 <= para.max_hp:
                        para.hp += 10
                        para.bag_item[i] -= 1
                    else:
                        para.hp = para.max_hp
                        para.bag_item[i] -= 1
            if i == "魔法草":
                if para.bag_item[i] >= 1:
                    if para.mp + 5 <= para.max_mp:
                        para.mp += 5
                        para.bag_item[i] -= 1
                    else:
                        para.mp = para.max_mp
                        para.bag_item[i] -= 1
            break
        else:
            check += 1
            continue

def use_equip(bg,point):

    check = 0

    from dateclass import para

    for i in list(para.equip_status.keys()):
        if check == point:
            if para.equip_status[i][0] == 0:
                if para.weapon[0] == 0:
                    para.weapon[0] = 1
                    para.weapon[1] = i
                    para.bag_equip[i] -= 1
                    para.attack += para.equip_status[i][1]
                else:
                    para.attack -= para.equip_status[para.weapon[1]][1]
                    para.bag_equip[para.weapon[1]] += 1
                    para.weapon[1] = i
                    para.bag_equip[i] -= 1
                    para.attack += para.equip_status[i][1]                    
            elif para.equip_status[i][0] == 1:
                if para.armor[0] == 0:
                    para.armor[0] = 1
                    para.armor[1] = i
                    para.bag_equip[i] -= 1
                    para.deffence += para.equip_status[i][1]
                else:
                    para.deffence -= para.equip_status[para.armor[1]][1]
                    para.bag_equip[para.armor[1]] += 1
                    para.armor[1] = i
                    para.bag_equip[i] -= 1
                    para.deffence += para.equip_status[i][1]
            break
        else:
            check += 1
            continue