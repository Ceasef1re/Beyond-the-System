#Add imports here (classes and stuff)
import ships

player = input("What is your name?\n> ")
print("Hi " + player + "!\n\n")

print(ships.s1.name + " is approaching!\n")
print("What would you like to do?\n1. Attack\n2. Flee\n")
choice = int(input("> "))

if choice == 1:
    print("Ship HP: " + str(ships.s1.hp))
elif choice == 2:
    print("You fled")



