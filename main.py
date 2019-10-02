import time
import ships

cooldownStart = 0


player = input("What is your name?\n> ")
print("Hi " + player + "!")
ships.playerShip.name = input("What would you like to name your ship?\n> ")
print(ships.playerShip.name + " it is!")

playerShip = ships.playerShip

print(ships.s1.name + " is approaching!\n")
print("What would you like to do?\n1. Attack\n2. Flee\n")
choice = input("> ")    

if choice == "1":
    print("You begun combat!")
    while True:
        choice = input("1. Fire\n> ")
        if choice == "1":
            selectedWeapon = playerShip.weapons[0]
            loop = 1
            print("")

            for weapon in playerShip.weapons:
                print(str(loop) + ". " + weapon.name)
                
                #ships.s1.hp -= playerShip.weapons[0].damage
                #print("You delt " + str(playerShip.weapons[0].damage) + " to enemy ship")
                #print(ships.s1.name + " is on " + str(ships.s1.hp) + " hp!")

                #if ships.s1.hp <= 0 or playerShip.hp <= 0:
                #    print("\nYou destroyed the enemy ship!")
                #    break;

                loop += 1

            choice = input("Choose a weapon:\n> ")
            loop = 1
            for weapon in playerShip.weapons:
                if choice == str(loop):
                    selectedWeapon = playerShip.weapons[loop - 1]

                loop += 1

            print(selectedWeapon.name)
        else:
            print("Invalid input")
        
elif choice == "2":
    print("You fled")
else:
    print("Invalid input")


