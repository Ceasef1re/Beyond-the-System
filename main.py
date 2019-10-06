import ships
import combat
import player

name = input("What is your name?\n> ")
print("Hi " + name + "!")
ships.playerShip.name = input("What would you like to name your ship?\n> ")
print(ships.playerShip.name + " it is!")

player = player.Player(name, 0)

print(ships.randShip.name + " is approaching!\n")
print("What would you like to do?\n1. Attack\n2. Flee\n")
choice = input("> ")    

if choice == "1":
    print("You begun combat!\n")
    combat.CombatStart(ships.randShip)
    
elif choice == "2":
    print("You fled")
else:
    print("Invalid input") #Loop back to choice because it breaks rn


