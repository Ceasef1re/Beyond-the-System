import ships
import weapons

enemy = "placeholder"

def CombatStart(enemyShip):
    Combat(enemyShip)

def Combat(enemyShip):
	#Start up all necessary functions for combat
	weapons.StartCooldowns()

	while True:
		choice = input("Select an option:\n1. Fire\n> ")
		if choice == "1":
			while True:
				selectedWeapon = "null"
				loop = 1
				print("\nChoose a weapon:")

				for weapon in ships.playerShip.weapons:
					print(str(loop) + ". " + weapon.name)
					loop += 1

				loop = 1
				choice = input("> ")
				for weapon in ships.playerShip.weapons:
					if choice == str(loop):
						selectedWeapon = ships.playerShip.weapons[loop - 1]
						break

					if (choice) > str(len(ships.playerShip.weapons)):
						print("Invalid option")
						break

					loop += 1
				if selectedWeapon != "null":
					break
    
			ships.weapons.Attack(selectedWeapon, enemyShip)

			if enemyShip.hp <= 0 or ships.playerShip.hp <= 0:
				print("\nYou destroyed the enemy ship!")
				break;
		else:
			print("Invalid input")

def Status(dmg):
	if(dmg > 0):
		print("Captain, we took " + str(dmg) + " damage!")
	
		if ships.playerShip.hp > 75:
			print(">75 hp")
			time.sleep(2)
		if ships.playerShip.hp > 50 and ships.playerShip.hp < 75:
			print(">50 hp")
			time.sleep(2)
		if ships.playerShip.hp > 25 and ships.playerShip.hp < 50:
			print (">25 hp")
			time.sleep(2)
	else:
		print("Captain, we avoided an attack!")
