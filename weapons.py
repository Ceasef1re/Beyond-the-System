import time

def StartCooldowns():
    return 0 #temporary

class Weapon:
    def __init__(self, name, minDmg, maxDmg, cooldown, hitLanes):
        self.name = name
        self.minDmg = minDmg
        self.maxDmg = maxDmg
        self.cooldown = cooldown
        self.hitLanes = hitLanes

availableWeapons = [Weapon("lasers", 1, 10, 10, 2),
                    Weapon("missile", 1, 15, 5, 3)]
lasers = availableWeapons[0]
missile = availableWeapons[1]
