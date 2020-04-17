import random


class bcolors:
    header = '\033[95m'
    okblue = '\033[94m'
    okgreen = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    endc = '\033[0m'
    bold= '\033[1m'
    underline = '\033[4m'

class person:
    def __init__(self,name,hp,mp,atk,df,magic,item):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.item = item
        self.actions = ["ATTACK","MAGIC","ITEM"]

    def generate_damage(self):
        return random.randrange(self.atkl,self.atkh)
    def generate_spelldamage(self,i):
        mgl = self.magic[i]["dmg"] - 5
        mgh = self.magic[i]["dmg"] + 5
        return random.randrange(mgl,mgh)
    def take_damage(self,dmg):
        self.hp = self.hp - dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp
    def get_hp(self):
        return self.hp
    def get_maxhp(self):
        return self.maxhp
    def get_mp(self):
        return self.mp
    def get_maxmp(self):
        return self.maxmp
    def reduce_cost(self,cost):
        self.mp = self.mp - cost

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        return self.hp

    def choose_magic(self):
        i = 1
        print( "\n" + bcolors.okblue + "SPELLS:" + bcolors.endc )
        for spell in self.magic:
            print( "    " + str( i ) + ":" + spell.name )
            i = i + 1

    def choose_item(self):
        i = 0
        y = 1
        for item in self.item:
            fiber = self.item[i]["item"].name
            descrip = self.item[i]["item"].description
            quantit = self.item[i]["item"].quantity
            print( str(y),". ", fiber , ":" , descrip , "(x" ,quantit  )
            i = i + 1
            y = y + 1
    def choose_action(self):
        i = 1
        print( "\n" + bcolors.okgreen + "ACTIONS:" + bcolors.endc )
        print(self.name + ":")
        for action in self.actions:
            print( "    " + str( i ) + ":" + action )
            i = i + 1
    def choose_target(self,enemies):
        x = 1
        i = 0
        print( "\n" + bcolors.fail + "TARGET:" + bcolors.endc )
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print(x,".",enemy.name)
                i += 1
                x += 1
        choice = int(input("    Choose target")) - 1
        return choice
    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp /self.maxhp) * 100/2
        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1
        while len(hp_bar) < 50:
            hp_bar += " "
        hp_string = str( self.hp ) + "/" + str( self.maxhp )
        current_hp = ""
        if len( hp_string ) < 11:
            decreased = 11 - len( hp_string )
            while decreased > 0:
                current_hp += " "
                decreased -= 1
            current_hp += hp_string
        else:
            current_hp = hp_string
        print( "NAME                  HP:                                       MP:" )
        print( "_________________________                  ___________" )
        print( self.name, current_hp, "|", hp_bar, "|")

    def get_stats(self):
        hp_bar = ""
        mp_bar = ""
        bar_ticks = (self.hp/self.maxhp) * 100/4
        mp_ticks = (self.mp/self.maxmp) * 100/10
        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1
        while len(hp_bar) < 25:
            hp_bar += " "
        while mp_ticks > 0:
            mp_bar+= "█"
            mp_ticks -= 1
        while len(mp_bar) < 10:
            mp_bar += " "
        hp_string = str(self.hp) + "/" +str(self.maxhp)
        current_hp = ""
        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)
            while decreased > 0:
                current_hp += " "
                decreased -= 1
            current_hp += hp_string
        else:
            current_hp = hp_string
        mp_string = str( self.hp ) + "/" + str( self.maxhp )
        current_mp = ""
        if len( mp_string ) < 7:
            decreased_mp = 7 - len( mp_string )
            while decreased_mp > 0:
                current_mp += " "
                decreased_mp -= 1
            current_mp += mp_string
        else:
            current_mp = mp_string

        print( "NAME                  HP:                                       MP:" )
        print( "_________________________                  ___________" )
        print( self.name , current_hp, "|",hp_bar,"|"  ,current_mp  , "|", mp_bar,"|")
    def get_enemy(self):
        pass



