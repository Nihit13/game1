from classes.game import person, bcolors
from classes.magic import spell
from classes.inventory import item
import  random
import datetime
print("\n\n")
print("NAME                  HP:                                       MP:"             )
print(               "_________________________                  ___________")
print("valos 460/460 |████████████████████████|         65/65   |███████████|")
print(               "_________________________                  ___________")
print("valos 460/460 |                         |        65/65   |           |")
print(               "_________________________                  ___________")
print("valos 460/460 |                         |         65/65  |           |")


#black magic
fire = spell("fire",10,100,"black")
thunder = spell("thunder",10,100,"black")
blizzard = spell("blizzard",10,100,"black")
meteor = spell("meteor",20,200,"black")
quake = spell("quake",14,140,"black")

#white magic
cure = spell("cure",10,100,"white")
cura = spell("cura",10,100,"white")

potion = item("potion","potion","heals 50 hp",50,15)
hipotion = item("hi-potion","potion","heals 100 hp",100,2)
superpotion = item("superpotion","potion","heals 500 hp",500,5)
elixer = item("elixer","elixer","fully restores hp/mp of one party member",9999,5)
mega_elixer = item("Mega elixer","elixer","fully restores party's hp/mp",9999,5)
grenade = item("grenade","attack","deals 500 damage",500,5)

player_spells = [fire,thunder,blizzard,meteor,quake,cure,cura]
player_items = [{"item": potion,"quantity":15},
                {"item":hipotion,"quantity":5},
               {"item":superpotion,"quantity":2},
                {"item":elixer,"quantity":5},
               {"item":mega_elixer,"quantity":5},
                {"item":grenade,"quantity":5}]



player1 = person("valos",3260,132,60,34,[fire,thunder,blizzard,meteor,quake,cure,cura],[{"item": potion,"quantity":15},
                {"item":hipotion,"quantity":5},
               {"item":superpotion,"quantity":2},
                {"item":elixer,"quantity":5},
               {"item":mega_elixer,"quantity":5},
                {"item":grenade,"quantity":5}])
player2 = person("nick",4160,188,60,34,[fire,thunder,blizzard,meteor,quake,cure,cura],[{"item": potion,"quantity":15},
                {"item":hipotion,"quantity":5},
               {"item":superpotion,"quantity":2},
                {"item":elixer,"quantity":5},
               {"item":mega_elixer,"quantity":5},
                {"item":grenade,"quantity":5}])
player3 = person("robot",3089,174,60,34,[fire,thunder,blizzard,meteor,quake,cure,cura],[{"item": potion,"quantity":15},
                {"item":hipotion,"quantity":5},
               {"item":superpotion,"quantity":2},
                {"item":elixer,"quantity":5},
               {"item":mega_elixer,"quantity":5},
                {"item":grenade,"quantity":5}])
players = [ player1,player2,player3]

enemy2 = person("Imp",1250,130,560,325,[],[])
enemy = person("Magus",12200,221,525,25,[],[])
enemy3 = person("Imp",1250,130,560,325,[],[])

enemies = [enemy,enemy2,enemy3]

i = 0
for item in player1.item:
    fiber = player1.item[i]["item"].name
    print(fiber)
    i = i + 1


running = True

while running:
    print("============================================================")
    print(bcolors.fail + bcolors.bold + "AN ENEMY CAME IN FRONT OF YOU " +bcolors.underline+ bcolors.endc)
    for player in players:

        player.get_stats()
        print("\n")
    for enemy in enemies:
        enemy.get_enemy_stats()

        
    for player in players:
        player.choose_action()
        choice = input("Choose action")
        if choice == -1:
            continue
        index = int(choice) - 1
        if index == 0:
           dmg = player.generate_damage()
           enemy = player.choose_target( enemies )
           enemies[enemy].take_damage(dmg)
           print("You attacked for ",dmg,"damage points","Enemy HP: ",enemies[enemy].get_hp())

        elif index == 1:
            player.choose_magic()
            spell_choice = int(input("choose magic:")) - 1
            if spell_choice == -1:
               continue
            spell = player.magic[spell_choice]
            spell_dmg = spell.generate_damage()
            current_mp = player.get_mp()
            player.reduce_cost( spell.cost )
            if spell.cost >current_mp:
                print(bcolors.fail + bcolors.bold + "You donot have enough MP cost" + bcolors.endc)
                continue
            if spell.type == "white":
                player.heal(spell_dmg)
                print(spell.name,"heals for ",spell_dmg)
            elif spell.type == "black":
                enemy = player.choose_target( enemies )
                enemies[enemy].take_damage( spell_dmg )
                print("You used ",spell.name,"you attacked for ",spell_dmg,"damage points","Enemy HP:",enemies[enemy].get_hp(),"Current MP :",player.get_mp())

        elif index == 2:
            player.choose_item()
            choice_item = int(input("Choose item")) - 1
            if choice_item == -1:
                continue

            item = player.item[choice_item]["item"]
            if item.quantity == 0:
                print(bcolors.fail + "None left " + bcolors.endc)
                continue
            item_name = player.item[choice_item]["item"].name
            item.quantity -= 1
            if item.name == mega_elixer:
                for y in players:
                    y.mp = y.maxmp
                    y.hp = y.maxhp
            if item.type == "potion":
                player.heal(item.prop)
                print(item_name,"heals for",item.prop,"damage")
            elif item.type == "elixer":
                player.hp = player.maxhp
                player.mp = player.maxmp
                print("MP and HP fully restored ")
            elif item.type == "attack":
                enemy = player.choose_target( enemies )
                enemies[enemy].take_damage( item.prop )
                print("You throwed a", item.name, "on the enemy . Your HP :", player.get_hp(),".Enemy HP :",enemies[enemy].get_hp())
        enemy_choice = 1
        print(bcolors.fail + bcolors.bold + "An enemy attacks" + bcolors.endc)
        target = random.randrange(0,3)
        enemy_dmg = enemy.generate_damage()
        players[target].take_damage(enemy_dmg)
        print( enemies[enemy].name," attacked for ", enemy_dmg,"damage points" ,"Your HP: ", player.get_hp())
        print("--------------------------")

        print("Your HP", bcolors.okgreen, player.get_hp(), "/", player.get_maxhp(), bcolors.endc)
        print("Your MP", bcolors.okblue, player.get_mp(), "/", player.get_maxmp(), bcolors.endc)
        defeated_enemies = 0
        defeated_players = 0
        for player in players :
            if player.get_hp() == 0:
                defeated_players += 1
        if defeated_players == 2:
            print(bcolors.fail + "You lose"+ bcolors.endc)
            running = False
        for enemy in enemies:
            if enemy.get_hp == 0:
                defeated_enemies += 1
        if defeated_enemies == 2:
            print(bcolors.okgreen + "You win "+ bcolors.endc)
            running = False
        if enemy.get_hp() == 0:
            print(bcolors.okgreen + "You win" +bcolors.endc)
            running = False
        elif player.get_hp() == 0:
                print(bcolors.fail + "THE ENEMY HAS DEFEATED YOU" + bcolors.endc)
                running = False