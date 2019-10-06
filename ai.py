import combat
import random
import math

def Attack(weapon):
    if weapon.hitLanes > 1:
        print("Attack incoming\n Choose a path to avoid it\n")
        for i in range(weapon.hitLanes):
            print(str(i + 1) + ".")

        while True:
            choice = input("> ")

            attackLane = random.randint(1, weapon.hitLanes)
            validOption = False

            if choice != str(attackLane):
                for i in range(weapon.hitLanes):
                    if choice == str(i):
                        dmg = random.randint(weapon.minDmg, weapon.maxDmg)
                        ships.playerShip.hp -= dmg
                
                        print("You delt " + str(dmg) + " damage to the enemy ship")
                        print(ships.playerShip.name + " is on " + str(ships.playerShip.hp) + " hp!\n")
                        validOption = True
                        break

                if not validOption:
                    print("Invalid option")
                
            else:
                chance = random.randint(1,10)
                if chance >= 9:
                    dmg = 0
                    print("Your attack missed")
                    print(ships.playerShip.name + " is on " + str(ships.playerShip.hp) + " hp!\n")
                elif chance >= 7 and chance < 9:
                    dmg = math.ciel(random.randint(weapon.minDmg, weapon.maxDmg)*0.25)
                    ships.playerShip.hp -= dmg
                    print("You dealt " + str(dmg) + " damage")
                    print(ships.playerShip.name + " is on " + str(ships.playerShip.hp) + " hp!\n")
                elif chance >= 1 and chance < 7:
                    dmg = math.ceil(random.randint(weapon.minDmg, weapon.maxDmg)*0.5)
                    ships.playerShip.hp -= dmg
                    print("You dealt " + str(dmg) + " damage")
                    print(ships.playerShip.name + " is on " + str(ships.playerShip.hp) + " hp!\n")

                else:
                    dmg = random.randint(weapon.minDmg, weapon.maxDmg)

                break
    
    combat.Status(dmg)
	
def Think():
	#if attack incoming, run DodgeAttack()
	#check cooldowns every second and if weapon off cooldown, fire weapon (Attack(weapon))
	#maybe some other stuff idk
	return 0 #temporary
	
def DodgeAttack(weapon, enemyShip):
	if weapon.hitLanes > 1:
		attackLane = random.randint(1, weapon.hitLanes)
		choice = random.randint(1, weapon.hitLanes)

		if choice != attackLane:
			dmg = random.randint(weapon.minDmg, weapon.maxDmg)
			enemyShip.hp -= dmg
	
			print("You delt " + str(dmg) + " damage to the enemy ship")
			print(enemyShip.name + " is on " + str(enemyShip.hp) + " hp!\n")
		else:
			chance = random.randint(1, 10)
			if chance >= 9:
				dmg = 0
				enemyShip.hp -= dmg
				print("Your attack missed")
			if chance >= 7 and chance < 9:
				dmg = math.ceil(random.randint(weapon.minDmg, weapon.maxDmg) * 0.25)
				print(dmg)
				enemyShip.hp -= dmg
				print("You dealt " + str(dmg) + " damage")
			if chance >= 1 and chance < 7:
				dmg = math.ceil(random.randint(weapon.minDmg, weapon.maxDmg) * 0.5)
				enemyShip.hp -= dmg
				print("You dealt " + str(dmg) + " damage")
				print(enemyShip.name + " is on " + str(enemyShip.hp) + " hp!\n")
	else:
		dmg = random.randint(weapon.minDmg, weapon.maxDmg)
		enemyShip.hp -= dmg
	
		print("You delt " + str(dmg) + " damage to the enemy ship")
		print(enemyShip.name + " is on " + str(enemyShip.hp) + " hp!\n")
