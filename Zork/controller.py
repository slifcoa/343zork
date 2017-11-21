# @author Adam Slifco
# @author Zack Hern

from player import Player
from neighborhood import Neighborhood
from observer import Observer

#########################################################
# Creates the neighboorhood and player objects.
# Also keeps track of homes and the total monster count
#########################################################
class Controller(Observer):

    ##################################################
    # Instantiates player and neighborhood objects
    ##################################################
    def __init__(self):
        super().__init__()

        self.playerOne = Player()

        self.neighborhood = Neighborhood(3)
        self.generatehouses()

    ##################################################
    # helper method to observe each house
    ##################################################
    def generatehouses(self):
        for street in self.neighborhood.houseList:
            for house in street:
                house.addObserver(self)


    #####################################################
    # Abstract Observer method. updates monster total
    #####################################################
    def update(self, other):
        self.neighborhood.totalMonsters -= 1
