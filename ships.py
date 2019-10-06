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

def createRandShip():
        randShip = Ship("random",
                    random.randint(1,100),
                    random.randint(1,100),
                    random.randint(1,10),
                    for i in range randShip.weaponNum:
                        random.choice(weapons.availableWeapons),
                    random.choice(["light", "medium", "heavy"]))
        return randShip

playerShip = Ship("",
                  100,
                  100,
                  2,
                  [weapons.availableWeapons[0], weapons.availableWeapons[1]],
                  "medium")

s1 = Ship("boop",
          100,
          100,
          2,
          [weapons.availableWeapons[0], weapons.availableWeapons[0]],
          "medium")

randShip = createRandShip()
