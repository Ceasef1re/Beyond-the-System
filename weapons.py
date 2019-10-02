class Weapon:
	def __init__(self, name, damage, cooldown, accuracy):
		self.name = name
		self.damage = damage
		self.cooldown = cooldown
		self.accuracy = accuracy

w1 = Weapon("lasers", 10, 10, 10)
w2 = Weapon("missile", 5, 5, 5)
