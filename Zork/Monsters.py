# @author Adam Slifco
# @author Zack Hern

from random import randrange, seed
from observable import Observable
from enum import Enum

# Factory concept obtained from https://pythonspot.com/en/factory-method/
# Originally overheard about the concept (accidental eavesdrop) from students in eosLab
# makes it easy to create new inherited subclasses

class Monsters(Observable):

    ####################################################################
    # "the factory method allows for easy addition of new subclasses.
    ####################################################################
    def factory(monType):
        if monType == "person": return Person()
        if monType == "zombie": return Zombie()
        if monType == "vampire": return Vampire()
        if monType == "ghoul": return Ghoul()
        if monType == "werewolf": return Werewolf()
        assert 0, "Invalid monType: " + monType
    factory = staticmethod(factory)

    ####################################################################
    # properly calculates the damage, Depending upon which weapon is used
    ####################################################################
    def mHit(self, attackData):
        isDead = False
        if self.monType == "person":
            damage = 0
        elif attackData["weaponType"] == self.useless[0]:
            damage = 0
        elif len(self.useless) == 2 and attackData["weaponType"] == self.useless[1]:
            damage = 0
        elif attackData["weaponType"] == self.weak:
            if self.monType == "zombie":
                damage = 2 * attackData["playerModifiedAttackPower"]

            if self.monType == "zombie":
                damage = 5 * attackData["playerModifiedAttackPower"]
                
        else:
            damage = attackData["playerModifiedAttackPower"]

        self.checkAlive(damage, isDead)
        return {"damage": damage, "dead": isDead}

    ############################
    # returns monsters power# 
    ############################
    def mAttacking(self):
        return self.attDamage

    ####################################################################
    # Checks too see if the monster is still alive after being hit
    ####################################################################
    def checkAlive(self, damage, isDead):
    
        self.currentHP -= damage

        if self.currentHP <= 0:
            super().update(self)
            isDead = True
        return {"damage": damage, "dead": isDead}

################################
# Inherited Monster classes# 
################################

class Ghoul(Monsters):
    def __init__(self):
        super().__init__()
        self.monType = "ghoul"
        seed()
        self.currentHP = randrange(40,80)
        self.attDamage = randrange(15,21)
        self.weak = "NerdBombs"
        self.useless = ["none"]

class Person(Monsters):
    def __init__(self):
        super().__init__()
        self.monType = "person"
        self.currentHP = 100
        self.attDamage = -10
        self.weak = "none"
        self.useless = ["none"]

class Vampire(Monsters):
    def __init__(self):
        super().__init__()
        self.monType = "vampire"
        seed()
        self.currentHP = randrange(100,200)
        self.attDamage = randrange(10,15)
        self.weak = "none"
        self.useless = ["ChocolateBar"]

class Werewolf(Monsters):
    def __init__(self):
        super().__init__()
        self.monType = "werewolf"
        seed()
        self.currentHP = 200
        self.attDamage = randrange(0, 40)
        self.weak = "none"
        self.useless = ["ChocolateBar", "SourStraw"]

class Zombie(Monsters):
    def __init__(self):
        super().__init__()
        self.monType = "zombie"
        seed()
        self.currentHP = randrange(50,100)
        self.attDamage = randrange(0,10)
        self.weak = "SourStraw"
        self.useless = ["none"]

####################################
# assigns int values to monsters
####################################
class MonsterTypes(Enum):
    person = 0
    zombie = 1
    vampire = 2
    ghoul = 3
    werewolf = 4