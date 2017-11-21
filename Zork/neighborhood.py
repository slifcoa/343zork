# @author Adam Slifco
# @author Zack Hern

from home import Home

#######################################################
# creates a grid and populates each cell with a home
#######################################################
class Neighborhood:

    ####################################################################
    # defines size of the neighborhood and instantiates the grid
    ####################################################################
    def __init__(self, size):
        super().__init__
        self.width = size
        self.length = size
        self.houseList = []
        self.totalMonsters = 0
        self.generateGrid()

    #############################################
    # helper function that populates the grid
    #############################################
    def generateGrid(self):
        for street in range(self.length):
            street = []
            self.houseList.append(street)
            for col in range(self.width):
                h = Home()
                self.monsterCount(len(h.monsters))
                street.append(h)

    #############################################
    # keeps track of total number of monsters
    #############################################
    def monsterCount(self, count):
        self.totalMonsters += count

