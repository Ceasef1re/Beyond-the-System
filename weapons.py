import random

def DealDamage(weapon):
      return random.randint(weapon.minDmg, weapon.maxDmg)

class Weapon:
	def __init__(self, name, minDmg, maxDmg, cooldown, accuracy):
		self.name = name
		self.minDmg = minDmg
		self.maxDmg = maxDmg
		self.cooldown = cooldown
		self.accuracy = accuracy

w1 = Weapon("lasers", 1, 10, 10, 10)
w2 = Weapon("missile", 1, 15, 5, 5)
