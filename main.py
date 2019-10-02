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
    print("You begun combat!\n")
    while True:
        choice = input("Select an option:\n1. Fire\n> ")
        if choice == "1":
            while True:
                selectedWeapon = "null"
                loop = 1
                print("\nChoose a weapon:")

                for weapon in playerShip.weapons:
                    print(str(loop) + ". " + weapon.name)
                    loop += 1

                loop = 1
                choice = input("> ")
                for weapon in playerShip.weapons:
                    if choice == str(loop):
                        selectedWeapon = playerShip.weapons[loop - 1]
                        break

                    if int(choice) > len(playerShip.weapons):
                        print("Invalid option")
                        break

                    loop += 1
                if selectedWeapon != "null":
                    break
    
            print("\nFiring " + selectedWeapon.name + "...")
            ships.s1.hp -= selectedWeapon.damage
            print("You delt " + str(selectedWeapon.damage) + " to enemy ship")
            print(ships.s1.name + " is on " + str(ships.s1.hp) + " hp!\n")

            if ships.s1.hp <= 0 or playerShip.hp <= 0:
                print("\nYou destroyed the enemy ship!")
                break;
        else:
            print("Invalid input")
elif choice == "2":
    print("You fled")
else:
    print("Invalid input")


