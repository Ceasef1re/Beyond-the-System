import weapons

class Ship:
	def __init__(self, name, hp, shields, weaponNum, weapons, armour):
		self.name = name
		self.hp = hp
		self.shields = shields
		self.wepNumber = weaponNum
		self.weapons = weapons
		self.armour = armour

playerShip = Ship("", 100, 100, 2, [weapons.w1, weapons.w2], "medium")
s1 = Ship("boop", 100, 100, 2, [weapons.w1, weapons.w2], "medium")
