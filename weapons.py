import random

def dmg(min, max):
      while True: return random.randint(min, max)

class Weapon:
	def __init__(self, name, damage, cooldown, accuracy):
		self.name = name
		self.damage = damage
		self.cooldown = cooldown
		self.accuracy = accuracy

w1 = Weapon("lasers", dmg(1,10), 10, 10)
w2 = Weapon("missile", dmg(1,15), 5, 5)
