import threading
import combat
import ai

class Weapon:
    def __init__(self, name, minDmg, maxDmg, cooldown, onCooldown, cooldownStart, hitLanes):
        self.name = name
        self.minDmg = minDmg
        self.maxDmg = maxDmg
        self.cooldown = cooldown
        self.onCooldown = onCooldown
        self.cooldownStart = cooldownStart
        self.hitLanes = hitLanes

availableWeapons = [Weapon("lasers", 1, 10, 10, False, 0, 2),
                    Weapon("missile", 1, 15, 5, False, 0, 3)]

lasers = availableWeapons[0]
missile = availableWeapons[1]
