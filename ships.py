import weapons

class Ship:
	def __init__(self, name, hp, wepNumber, weapons, defences):
		self.name = name
		self.hp = hp
		self.wepNumber = wepNumber
		self.weapons = weapons
		self.defences = defences

playerShip = Ship("", 100, 2, [weapons.w1, weapons.w2], "medium")
s1 = Ship("boop", 100, 2, [weapons.w1, weapons.w2], "medium")