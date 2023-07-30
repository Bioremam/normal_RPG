from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import time
import sys
import random

pygame.init()
black = (0,0,0)
white = (255,255,255)
message = [""]*10
font = pygame.font.Font('ipaexg00401/ipaexg.ttf', 20)
backimg = pygame.image.load("backimg/battle_map1.jpg")
slime = pygame.image.load("image/slime.png")

def init_message():
    for i in range(10):
        message[i] = ""

def set_message(msg):
    for i in range(10):
        if message[i] == "":
            message[i] = msg
            return
    for i in range(9):
        message[i] = message[i+1]
    message[9] = msg

def draw_msg(bg,txt,x,y,fnt,col):
    sur = fnt.render(txt,True,col)
    bg.blit(sur,[x+5,y+5])

def draw_status_inbattle(bg):

    from dateclass import para

    bg.fill(black,(0,520,200,200))
    pygame.draw.rect(bg,white,(0,520,200,200),width = 5,border_radius = 5)

    #hp
    pygame.draw.rect(bg,(255,138,197),(20,550,100,10)) #ピンク
    nowhp_rate = (para.hp/para.max_hp)*100
    pygame.draw.rect(bg,(0,208,0),(20,550,nowhp_rate,10)) #緑
    text = font.render("HP  {} / {}".format(para.hp,para.max_hp),True,white)
    bg.blit(text,(40,580))

    #mp
    pygame.draw.rect(bg,(142,219,255),(20,645,100,10)) #水色
    nowmp_rate = (para.mp/para.max_mp)*100
    pygame.draw.rect(bg,(5,69,255),(20,645,nowmp_rate,10)) #青色
    text = font.render("MP  {} / {}".format(para.mp,para.max_mp),True,white)
    bg.blit(text,(40,675))

def draw_msg_back(bg):

    bg.fill(black,(0,0,250,250))
    pygame.draw.rect(bg,white,(0,0,250,250),width = 5,border_radius = 5)

def battle_command(bg,point):

    bg.fill(black,(200,520,520,200))
    pygame.draw.rect(bg,white,(200,520,520,200),width = 5,border_radius = 5)
    
    sur = font.render("戦う",True,white)
    bg.blit(sur,[330,570])
    sur = font.render("呪文",True,white)
    bg.blit(sur,[330,650])
    sur = font.render("道具",True,white)
    bg.blit(sur,[590,570])
    sur = font.render("逃げる",True,white)
    bg.blit(sur,[590,650])

def after_battle_msg(bg):

    draw_msg_back(bg)
    for i in range(10):
        draw_msg(bg,message[i],0,24*i,font,white)
    pygame.display.update()

def draw_skill_back(bg):

    bg.fill(black,(0,250,250,270))
    pygame.draw.rect(bg,white,(0,250,250,270),width = 5,border_radius = 5)

def draw_item(bg):
    
    from dateclass import para
    point = 0

    for key in para.bag_item.keys():
        text = font.render('{}               {} 個'.format(key,para.bag_item[key]),True,white)
        bg.blit(text,(5,255+point*23))
        point += 1

def item_select(bg):

    '''draw_item(bg)
    draw_msg_back(bg)
    for i in range(10):
        draw_msg(bg,message[i],0,24*i,font,white)'''

    from dateclass import para,judge
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
                    if point < 3:
                        point += 1       
        
        key = pygame.key.get_pressed()

        if key[pygame.K_f] == 1:
            if not para.is_move:
                if point == 2:
                    para.is_move = True
                    para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                    pygame.display.update()
                    break
                
                if point == 0:
                    para.is_move = True
                    para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                    use_item(bg,point)
                    break
                
                if point == 1:
                    para.is_move = True
                    para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                    use_item(bg,point)
                    break
        
        if para.is_move and pygame.time.get_ticks() > para.move_delay:
            para.is_move = False


        draw_skill_back(bg)
        draw_item(bg)

        now = 255+point*23
        pygame.draw.rect(bg,white,(5,now,240,23),width = 1,border_radius = 5)

        pygame.display.update()

def use_item(bg,point):

    check = 0

    from dateclass import para,judge

    for i in list(para.bag_item.keys()):
        if check == point:
            if i == "薬草":
                if para.bag_item[i] >= 1:
                    judge.status = 1
                    if para.hp + 10 <= para.max_hp:
                        para.hp += 10
                        para.bag_item[i] -= 1
                    else:
                        para.hp = para.max_hp
                        para.bag_item[i] -= 1
            if i == "魔法草":
                if para.bag_item[i] >= 1:
                    judge.status = 1
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

def battle_scene(bg):

    from dateclass import para,judge

    idx = 10
    timer = 0
    point = 0
    ene_hp = random.randint(100,150)
    exp = int(ene_hp*(1.1))

    clock = pygame.time.Clock()
    init_message()

    while True:
        bg.blit(backimg,[0,0])
        draw_status_inbattle(bg)
        draw_skill_back(bg)
        after_battle_msg(bg)
        bg.blit(slime,[400,200])

        my_at = para.attack+random.randint(30,50)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    if point == 1:
                        point = 0
                    if point == 3:
                        point = 2

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    if point == 0:
                        point = 1
                    if point == 2:
                        point = 3    

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    if point == 2:
                        point = 0
                    if point == 3:
                        point = 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    if point == 0:
                        point = 2
                    if point == 1:
                        point = 3 
        
        
        battle_command(bg,point)
        key = pygame.key.get_pressed()
            
        if point == 0:
            sur = font.render("->",True,white)
            bg.blit(sur,[300,570])
        if point == 1:
            sur = font.render("->",True,white)
            bg.blit(sur,[300,650])
        if point == 2:
            sur = font.render("->",True,white)
            bg.blit(sur,[560,570])
        if point == 3:
            sur = font.render("->",True,white)
            bg.blit(sur,[560,650])
        
        
        timer += 1
        
        if idx == 10:
            if timer == 1:
                set_message("モンスターが現れた!")
            if timer == 6:
                idx += 1
                timer = 0
        
        elif idx == 11:
            if timer == 1:
                set_message("どうする？")
                idx += 1
                timer = 0
        
        elif idx == 12:
            if key[pygame.K_f] == 1:
                if point == 0:
                    set_message("あなたの攻撃!")
                    set_message("{} ダメージ!".format(my_at))
                    ene_hp -= my_at
                    if ene_hp <= 0:
                        set_message("モンスターを倒した!")
                        set_message("{}経験値ゲットした!".format(exp))
                        para.get_exp += exp
                        while para.get_exp >= para.lv_up:
                            para.lv += 1
                            para.get_exp -= para.lv_up
                            para.lv_up *= 3
                            para.attack += 2
                            para.deffence += 2
                        after_battle_msg(bg)
                        time.sleep(2)
                        break
                    else:
                        idx += 1
                        timer = 0
                if point == 1: #呪文
                    set_message("{} ダメージ!".format(my_at))
                    ene_hp -= my_at
                    idx += 1
                    timer = 0
                    if ene_hp <= 0:
                        set_message("モンスターを倒した!")
                        set_message("{}経験値ゲットした!".format(exp))
                        para.get_exp += exp
                        while para.get_exp >= para.lv_up:
                            para.lv += 1
                            para.get_exp -= para.lv_up
                            para.lv_up *= 3
                            para.attack += 2
                            para.deffence += 2
                        after_battle_msg(bg)
                        time.sleep(2)
                        break
                if point == 2: #道具
                    if not para.is_move:
                        para.is_move = True
                        para.move_delay = pygame.time.get_ticks() + para.move_delay_time
                        if len(para.bag_item) != 0:
                            item_select(bg)
                    if judge.status == 1:
                        idx += 1
                        timer = 0
                        judge.status = 0
                if point == 3: #逃げる
                    set_message("あなたは逃げ出した!")
                    d = random.randint(0,10)
                    if d+para.lv >= 5:
                        set_message("逃げ切れた!")
                        after_battle_msg(bg)
                        time.sleep(2)
                        break
                    else:
                        set_message("逃げられなかった!")
                        idx += 1
                        timer = 0
        elif idx == 13:
            if timer == 1:
                set_message("敵の攻撃!")
            if timer == 6:
                idx += 1
                timer = 0
        elif idx == 14:
            if timer == 1:
                ene_atk = random.randint(2,5)
                set_message("{} ダメージ!".format(ene_atk))
                if para.hp - ene_atk < 0:
                    para.hp = 0
                    idx = 4
                else:
                    para.hp -= ene_atk
            if timer == 6:
                idx += 1
                timer = 0
        
        elif idx == 4: #敗北処理
            set_message("あなたは倒れてしまった...")
            after_battle_msg(bg)
            time.sleep(2)
            break
        
        else:
            idx = 11
            timer = 0
        
        if point == 2:
            draw_item(bg)
        
        #after_battle_msg(bg)

        if para.is_move and pygame.time.get_ticks() > para.move_delay:
            para.is_move = False
        
        pygame.display.update()

        clock.tick(60)












