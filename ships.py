class Ship:
  def __init__(self, name, hp, weapons, defences):
    self.name = name
    self.hp = hp
    self.weapons = weapons
    self.defences = defences

s1 = Ship("boop", 100, 2, "medium")