import weapons
import random

class Ship:
    def __init__(self, name, hp, shields, weaponNum, weapons, armourIndex, armour):
        self.name = name
        self.hp = hp
        self.shields = shields
        self.weaponNum = weaponNum
        self.weapons = weapons
        self.armourIndex = armourIndex
        self.armour = armour

armour = ["weak", "light", "medium", "heavy", "special1", "special2", "special3"]

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
                    0,
                    armour.index(random.choice(armour)),
                    random.choice(armour))
        
        randShip.weapons = [random.choice(weapons.availableWeapons)]
        
        for i in range(randShip.weaponNum - 1):            
            randShip.weapons.append(random.choice(weapons.availableWeapons))

        return randShip

playerShip = Ship("", 100, 100,
                  2, [weapons.availableWeapons[0], weapons.availableWeapons[1]], armour.index("medium"), armour[armour.index("medium")])

s1 = Ship("boop", 100, 100,
          2, [weapons.availableWeapons[0], weapons.availableWeapons[0]], armour.index("medium"), armour[armour.index("medium")])

randShip = createRandShip()
