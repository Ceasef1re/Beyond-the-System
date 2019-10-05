import weapons

class Ship:
	def __init__(self, name, hp, shields, weaponNum, weapons, armour):
		self.name = name
		self.hp = hp
		self.shields = shields
		self.wepNumber = weaponNum
		self.weapons = weapons
		self.armour = armour

def createRandShip():
        randShipWep = random.choice(weapons.availableWeapons)
        randShip = Ship("random",
                    random.randint(1,100),
                    random.randint(1,100),
                    random.randint(1,10),
                    randShipWep,
                    random.choice(["light", "medium", "heavy"]))
        return randShip

playerShip = Ship("", 100, 100, 2, [weapons.w1, weapons.w2], "medium")
s1 = Ship("boop", 100, 100, 2, [weapons.w1, weapons.w2], "medium")
randShip = createRandShip()
