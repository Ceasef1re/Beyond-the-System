import weapons
import random

class Ship:
    def __init__(self, name, hp, shields, weaponNum, weapons, armour):
        self.name = name
        self.hp = hp
        self.shields = shields
        self.wepNumber = weaponNum
        self.weapons = weapons
        self.armour = armour

name1 = ["Blazing ", "Mercenary ", "Battle ", "Resilient ",
         "Iron-Side ", "Crimson ", "Final ", "Steel ",
         "Black ", "New ", "Galactic ", "Invincible ",
         "Opal ", "Silent ", "Maiden ", "Fire ",
         "Close ", "Wailing ", "Dark ", "Ark "]

name2 = ["Thorn", "Star", "Mercury", "Ambasador",
         "Valkyrie", "Cruiser", "Frontier", "Aurora",
         "Cloud", "Hope", "Core", "World",
         "Titan", "Wyvern", "Voyager", "Fury",
         "Encounter", "Talon", "Wind", "Phoenix"]

def createRandShip():
        randShip = Ship("The " + random.choice(name1) + random.choice(name2),
                    random.randint(1,100),
                    random.randint(1,100),
                    random.randint(1,10),
                    random.choice(weapons.availableWeapons),
                    random.choice(["light", "medium", "heavy"]))
        return randShip

playerShip = Ship("", 100, 100,
                  2, [weapons.availableWeapons[0], weapons.availableWeapons[1]], "medium")

s1 = Ship("boop", 100, 100,
          2, [weapons.availableWeapons[0], weapons.availableWeapons[0]], "medium")

randShip = createRandShip()
