import ships
import combat

cooldownStart = 0

player = input("What is your name?\n> ")
print("Hi " + player + "!")
ships.playerShip.name = input("What would you like to name your ship?\n> ")
print(ships.playerShip.name + " it is!")

print(ships.s1.name + " is approaching!\n")
print("What would you like to do?\n1. Attack\n2. Flee\n")
choice = input("> ")    

if choice == "1":
    print("You begun combat!\n")
    combat.CombatStart(ships.s1)
             
elif choice == "2":
    print("You fled")
else:
    print("Invalid input") #Loop back to choice because it breaks rn


