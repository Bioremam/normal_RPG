class Date():

    def __init__(self):
        
        file = open("savedate.txt","r")
        rl = file.readlines()
        file.close()
        
        self.mapdate = eval(rl[0].strip("\n")) #リスト型でマップ情報管理
        if len(self.mapdate) == 0:
            for i in range(32):
                self.mapdate.append([0]*32)
        self.map = int(rl[1].strip("\n")) #マップを数字で管理
        self.pl_x = int(rl[2].strip("\n")) #x座標
        self.pl_y = int(rl[3].strip("\n")) #y座標
        self.direction = int(rl[4].strip("\n")) #主人公の方向を管理 12時の方向から時計回りに0,1,2,3
        self.is_move = (rl[5].strip("\n"))
        self.move_delay = int(rl[6].strip("\n"))
        self.move_delay_time = int(rl[7].strip("\n"))
        

    def savefile(self):
        file = open("save.txt","w")
        file.write(str(self.get_exp)+"\n")
        file.close()

para = Date()