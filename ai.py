import combat
import random
import math

def Attack(weapon):
	if weapon.hitLanes > 1:
		choice = input("Attack incoming!\nChoose a path to avoid it!\n1.\n2,\n3.\n> ")
		attackLane = random.randint(1, weapon.hitLanes)

		if int(choice) == attackLane:
			dmg = random.randint(weapon.minDmg, weapon.maxDmg)
		else:
			dmg = 0;
	else:
		dmg = random.randint(weapon.minDmg, weapon.maxDmg)
	
	combat.Status(dmg)
	return dmg
	
def Think():
	#if attack incoming, run DodgeAttack()
	#check cooldowns every second and if weapon off cooldown, fire weapon (Attack(weapon))
	#maybe some other stuff idk
	return 0 #temporary
	
def DodgeAttack(weapon, enemyShip):
	if weapon.hitLanes > 1:
		attackLane = random.randint(1, weapon.hitLanes)
		choice = random.randint(1, weapon.hitLanes)

		if int(choice) != attackLane:
			dmg = random.randint(weapon.minDmg, weapon.maxDmg)
			enemyShip.hp -= dmg
	
			print("You delt " + str(dmg) + " damage to the enemy ship")
			print(enemyShip.name + " is on " + str(enemyShip.hp) + " hp!\n")
		else:
			chance = random.randint(1, 10)
			if chance >= 9:
				dmg = 0
				print("Your attack missed")
			if chance >= 7 and chance < 9:
				dmg = math.ceil(random.randint(weapon.minDmg, weapon.maxDmg) * 0.25)
				print(dmg)
				print("You dealt " + str(dmg) + " damage")
			if chance >= 1 and chance < 7:
				dmg = math.ceil(random.randint(weapon.minDmg, weapon.maxDmg) * 0.5)
				print("You dealt " + str(dmg) + " damage")
				print(enemyShip.name + " is on " + str(enemyShip.hp) + " hp!\n")
	else:
		dmg = random.randint(weapon.minDmg, weapon.maxDmg)
		enemyShip.hp -= dmg
	
		print("You delt " + str(dmg) + " damage to the enemy ship")
		print(enemyShip.name + " is on " + str(enemyShip.hp) + " hp!\n")
