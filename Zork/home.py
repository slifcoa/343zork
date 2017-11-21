# @author Adam Slifco
# @author Zack Hern

from observer import Observer
from observable import Observable
from Monsters import Monsters, MonsterTypes
from random import randrange, seed

######################################################
# Populates homes with monsters, and observes them
######################################################
class Home(Observable, Observer):

    ##########################################
    # generates random number of monsters
    ##########################################
    def __init__(self):
        super().__init__()
        seed()
        self.monsters = []
        self.generateMonsters()
        self.monsterCount()

    ######################################################
    # helper method that populates monsters into homes
    ######################################################
    def generateMonsters(self):
        monsterAmount = randrange(1,6)

        for i in range(monsterAmount):
            # represents the type of monster to be created
            monsterRand = randrange(1, 5)

            monster = Monsters.factory(MonsterTypes(monsterRand).name)
            self.monsters.append(monster)
            monster.addObserver(self)

    #################################################
    # helper method that counts monsters in home
    #################################################
    def monsterCount(self):
        self.monstersRem = len(self.monsters)

    #####################################################################
    # abstract update observer method. Keeps track of monsters in each house
    #####################################################################
    def update(self, other):
        self.monsters.remove(other)
        self.monstersRem -= 1
        self.monsters.append(Monsters.factory("person"))
        super().update(self)

