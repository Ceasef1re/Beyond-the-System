import weapons
import random
import combat
import ships
import math

def Attack(weapon):
    if weapon.hitLanes > 1:
        print("Attack incoming\n Choose a path to avoid it\n")
        for i in range(weapon.hitLanes):
            print(str(i + 1) + ".")
        choice = input("> ")

        attackLane = random.randint(1, weapon.hitLanes)

        if type(choice) is str:
            print("invalid option")
        elif int(choice) != attackLane:
            dmg = random.randint(weapon.minDmg, weapon.maxDmg)
            ships.playerShip.hp -= dmg
    
            print("You delt " + str(dmg) + " damage to the enemy ship")
            print(ships.playerShip.name + " is on " + str(ships.playerShip.hp) + " hp!\n")
        else:
            chance = random.randint(1,10)
            if chance == 9 or chance > 9:
                dmg = 0
                print("your attack missed")
            elif chance == 7 or chance > 7 and chance < 9:
                dmg = math.ciel(random.randint(weapon.minDmg, weapon.maxDmg)*0.25)
                print(dmg)
                print("you dealt " + str(dmg) + " damage")
            elif chance == 1 or chance > 1 and chance < 7:
                dmg = math.ceil(random.randint(weapon.minDmg, weapon.maxDmg)*0.5)
                print("you dealt " + str(dmg) + " damage")
                print(ships.playerShip.name + " is on " + str(ships.playerShip.hp) + " hp!\n")

            else:
                dmg = random.randint(weapon.minDmg, weapon.maxDmg)
    
    combat.Status(dmg)

Attack(weapons.w2)
