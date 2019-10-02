import time
import ships

cooldownStart = 0


player = input("What is your name?\n> ")
print("Hi " + player + "!")
ships.playerShip.name = input("What would you like to name your ship?\n> ")
print(ships.playerShip.name + " it is!")

print(ships.s1.name + " is approaching!\n")
print("What would you like to do?\n1. Attack\n2. Flee\n")
choice = input("> ")    

if choice == "1":
    print("You begun combat!")
    while True:
        choice = input("1. Fire\n> ")
        if choice == "1":
            ships.s1.hp -= ships.playerShip.weapons[0].damage
            print("You delt " + str(ships.playerShip.weapons[0].damage) + " to enemy ship")
            print(ships.s1.name + " is on " + str(ships.s1.hp) + " hp!")

            if ships.s1.hp <= 0 or ships.playerShip.hp <= 0:
                print("\nYou destroyed the enemy ship!")
                break;
        else:
            print("Invalid input")
        
elif choice == "2":
    print("You fled")
else:
    print("Invalid input")


