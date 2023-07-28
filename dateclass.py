import ast
from collections import defaultdict
import json

class Date():

    def __init__(self):
        
        file = open("savedate.txt","r")
        rl = file.readlines()
        file.close()

        with open("savedate_item.json","r",encoding='utf-8') as f:
            item = json.load(f)

        with open("savedate_equip.json","r",encoding='utf-8') as f:
            equip = json.load(f)

        
        self.mapdate = eval(rl[0].strip("\n")) #リスト型でマップ情報管理
        self.map = int(rl[1].strip("\n")) #マップを数字で管理
        self.pl_x = int(rl[2].strip("\n")) #x座標
        self.pl_y = int(rl[3].strip("\n")) #y座標
        self.direction = int(rl[4].strip("\n")) #主人公の方向を管理 12時の方向から時計回りに0,1,2,3
        self.is_move = (rl[5].strip("\n"))
        self.move_delay = int(rl[6].strip("\n"))
        self.move_delay_time = int(rl[7].strip("\n"))
        self.hp = int(rl[8].strip("\n"))
        self.max_hp = int(rl[9].strip("\n"))
        self.mp = int(rl[10].strip("\n"))
        self.max_mp = int(rl[11].strip("\n"))
        self.attack = int(rl[12].strip("\n"))
        self.deffence = int(rl[13].strip("\n"))
        self.money = int(rl[14].strip("\n"))
        #self.bag_item = item
        #self.bag_equip = equip
        #self.bag_item = ast.literal_eval(rl[15].strip("\n"))
        self.bag_item = defaultdict(lambda:0,item)
        self.bag_equip = defaultdict(lambda:0,equip)
        #self.bag_equip = ast.literal_eval(rl[16].strip("\n"))
        #self.bag_equip = defaultdict(int)

    def savefile(self):
        para.move_delay = 0
        file = open("savedate.txt","w")
        file.write(str(self.mapdate)+"\n")
        file.write(str(self.map)+"\n")
        file.write(str(self.pl_x)+"\n")
        file.write(str(self.pl_y)+"\n")
        file.write(str(self.direction)+"\n")
        file.write(str(self.is_move)+"\n")
        file.write(str(self.move_delay)+"\n")
        file.write(str(self.move_delay_time)+"\n")
        file.write(str(self.hp)+"\n")
        file.write(str(self.max_hp)+"\n")
        file.write(str(self.mp)+"\n")
        file.write(str(self.max_mp)+"\n")
        file.write(str(self.attack)+"\n")
        file.write(str(self.deffence)+"\n")
        file.write(str(self.money)+"\n")
        with open("savedate_item.json","w",encoding='utf-8') as f:
            json.dump(self.bag_item,f,ensure_ascii=False,indent = 4)
        with open("savedate_equip.json","w",encoding='utf-8') as f:
            json.dump(self.bag_equip,f,ensure_ascii=False,indent = 4)
        #file.write(str(self.bag_item)+"\n")
        #file.write(str(self.bag_equip)+"\n")
        file.close()

para = Date()