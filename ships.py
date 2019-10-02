class Ship:
  def __init__(self, name, hp, weapons, defences):
    self.name = name
    self.hp = hp
    self.weapons = weapons
    self.defences = defences

s1 = Ship("player", 100, 2, "medium")
s2 = Ship("boop", 100, 2, "medium")