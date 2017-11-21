# @author Adam Slifco
# @author Zack Hern

from Weapons import Weapon
from random import randrange, seed, uniform

class Player:

    ##################################################################
    # Defines player's power, health, and populates weapons stock.
    ##################################################################
    def __init__(self):
        seed()
        self.attackPower = randrange(10, 21)
        self.playerHP = randrange(100, 126)
        self.stock = []
        self.weaponGenerator()

    ########################################################################
    # calculates players attack value accordingly. factors in the specific 
    # weapon being used.
    ########################################################################
    def pAttack(self, weapon):
        attackData = {"playerBaseAttackPower": self.attackPower,
                      "playerModifiedAttackPower": self.attackPower * weapon.aModifier,
                      "weaponType": weapon.weapType}
        if weapon.ammo != float('inf'):
            pass
        if weapon.ammo == 0:
            self.stock.remove(weapon)
        return attackData

    ##########################################################################
    # calculates how much damage is dealt to player when a monster strikes
    ##########################################################################
    def pHit(self, monsterDamage):
        self.playerHP -= monsterDamage
        if self.playerHP <= 0:
            return "dead"
        return "alive"

    ####################################
    # Randomly generates 10 weapons
    ####################################
    def weaponGenerator(self):
        self.stock.append(Weapon.factory("hersheykiss"))
        for i in range(1, 10):
            seed()
            wepGen = randrange(1, 4)
            if wepGen == 1:
                self.stock.append(Weapon.factory("sourstraw"))
            elif wepGen == 2:
                self.stock.append(Weapon.factory("chocolatebar"))
            else:
                self.stock.append(Weapon.factory("nerdbomb"))

