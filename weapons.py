class Weapon:
  def __init__(self, damage, cooldown, accuracy):
    self.damage = damage
    self.cooldown = cooldown
    self.accuracy = accuracy

w1 = Weapon(10,10,10)
w2 = Weapon(5,5,5)