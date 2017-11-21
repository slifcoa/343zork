# @author Adam Slifco
# @author Zack Hern

from controller import Controller
import pygame

########################################
# Game class handles all GUI events
########################################

class Game:

    #############################
    # Instantiates the GUI
    #############################
    def __init__(self):
        self.controller = Controller()

        self.windowWidth = 600
        self.windowHeight = 900

        pygame.init()
        pygame.display.set_caption("Zork's Conquest")
        self.createColor()
        self.spriteStore = {}
        self.screen = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        self.clock = pygame.time.Clock()

        self.genImages()
        self.nMap = []
        self.genGrid()

        self.gameOver = False

    ########################################################################
    # Run function continues the game until is invoked to be done. Obtained
    # this run concept from https://stackoverflow.com/questions/16301193/
    # whats-the-proper-way-to-write-a-game-loop-in-python#
    ########################################################################
    def run(self):
        gameExit = False
        FPS = 13
        playerX = 200
        playerY = 100
        nextMove = "s"
        playerXChange = 0
        playerYChange = 0
        counter = 0
        held = False
        movementRate = 35
        onController = True
        isFighting = False
        player = self.getImage("assets/player.jpg")
        fightOngoing = False

        while not gameExit:
            self.clock.tick(FPS)

            while self.gameOver:
                self.screen.fill(self.black)
                self.displayData("Game Over", self.red, 300, 450)
                self.displayData("Do you want to Play again?: [Y]  [N]", self.white, 300, 450)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_y:
                            self.controller = Controller()
                            onController = True
                            isFighting = False
                            self.gameOver = False
                            self.run()
                        if event.key == pygame.K_n:
                            pygame.quit()
                            quit()

            if onController:
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w:
                            nextMove = "n"
                            held = True
                            playerYChange = -movementRate
                        if event.key == pygame.K_a:
                            nextMove = "w"
                            held = True
                            playerXChange = -movementRate

                        if event.key == pygame.K_s:
                            nextMove = "s"
                            held = True
                            playerYChange = movementRate

                        if event.key == pygame.K_d:
                            nextMove = "e"
                            held = True
                            playerXChange = movementRate

                        if event.key == pygame.K_RETURN:
                            if self.currentHouse.monstersRem > 0:
                                onController = False
                                isFighting = True
                                continue
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_w or event.key == pygame.K_s:
                            playerYChange = 0
                            held = False
                        if event.key == pygame.K_a or event.key == pygame.K_d:
                            playerXChange = 0
                            held = False

                playerX += playerXChange
                playerY += playerYChange

                self.curLocation(nextMove, playerX, playerY)
                self.currentHouse = self.controller.neighborhood.houseList[self.currRow][self.currCol]

                self.screen.blit(self.bg, (0, 0))
                self.screen.blit(player, (playerX, playerY))

                self.totalMonsters()
                self.homeData(playerX, playerY)
                self.displayData("Hit ENTER to move into this home", self.black, 300, 0)

                pygame.display.update()

            if isFighting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_0:
                            self.fight(self.controller.playerOne.stock[
                                                 0])
                            fightOngoing == True
                        if event.key == pygame.K_1 and len(self.controller.playerOne.stock) >= 2:
                            self.fight(self.controller.playerOne.stock[1])
                            fightOngoing == True
                        if event.key == pygame.K_2 and len(self.controller.playerOne.stock) >= 3:
                            self.fight(self.controller.playerOne.stock[2])
                            fightOngoing == True
                        if event.key == pygame.K_3 and len(self.controller.playerOne.stock) >= 4:
                            self.fight(self.controller.playerOne.stock[3])
                            fightOngoing == True
                        if event.key == pygame.K_4 and len(self.controller.playerOne.stock) >= 5:
                            self.fight(self.controller.playerOne.stock[4])
                            fightOngoing == True
                        if event.key == pygame.K_5 and len(self.controller.playerOne.stock) >= 6:
                            self.fight(self.controller.playerOne.stock[5])
                            fightOngoing == True
                        if event.key == pygame.K_6 and len(self.controller.playerOne.stock) >= 7:
                            self.fight(self.controller.playerOne.stock[6])
                            fightOngoing == True
                        if event.key == pygame.K_7 and len(self.controller.playerOne.stock) >= 8:
                            self.fight(self.controller.playerOne.stock[7])
                            fightOngoing == True
                        if event.key == pygame.K_8 and len(self.controller.playerOne.stock) >= 9:
                            self.fight(self.controller.playerOne.stock[8])
                            fightOngoing == True
                        if event.key == pygame.K_9 and len(self.controller.playerOne.stock) == 10:
                            self.fight(self.controller.playerOne.stock[9])
                            fightOngoing == True

                self.screen.fill(self.black)
                self.screen.blit(self.battleBG, (0, 200))
                self.screen.fill(self.white, rect=[650, 700, 10, 250])
                self.screen.fill(self.white, rect=[650, 700, 250, 10])
                self.screen.fill(self.white, rect=[900, 700, 10, 250])
                self.screen.fill(self.lightblue, rect=[660, 710, 240, 240])
                self.displayData("Zork", self.white, 680, 730)
                self.displayData("HP: " + repr(self.controller.playerOne.playerHP), self.white, 680, 790)
                self.displayMonsters()
                self.printWeapons()

                self.clock.tick(5)
                pygame.display.update()

    pygame.quit()

    ##################################################
    #positions, styles, and displays str message
    ##################################################
    def displayData(self, msg, color, x, y):
        text = self.font.render(msg, True, color)
        self.screen.blit(text, (x, y))

    ###############################################
    #prints the total amount of monsters left
    ###############################################
    def totalMonsters(self):
        totalMonsters = self.controller.neighborhood.totalMonsters
        msg = repr(totalMonsters) + " monsters are still haunting the neighborhood"
        self.displayData(msg, self.black, 300, 15)

    ##################################################
    # uses sprite storing to load images in pygame
    ##################################################
    def getImage(self, key):
        if key not in self.spriteStore:
            self.spriteStore[key] = pygame.image.load(key)
        return self.spriteStore[key]

    ##########################################
    # keeps track of the players location
    ##########################################
    def curLocation(self, nextMove, playerX, playerY):
        if nextMove == "e" or nextMove == "w":
            if  playerX > 0 and playerX < self.colLen:
                self.currCol = 0
            elif playerX > self.colLen and playerX < self.colLen * 2:
                self.currCol = 1
            elif playerX > self.colLen*2 and playerX < self.colLen * 3:
                self.currCol = 2
            elif playerX > self.colLen*3 and playerX < self.colLen * 4:
                self.currCol = 3
            elif playerX > self.colLen*4 and playerX < self.colLen * 5:
                self.currCol = 4

        elif nextMove == "n" or nextMove == "s":
            if  playerY > 0 and playerY < self.rowLen:
                self.currRow = 0
            elif playerY > self.rowLen and playerY < self.rowLen * 2:
                self.currRow = 1
            elif playerY > self.rowLen*2 and playerY < self.rowLen * 3:
                self.currRow = 2
            elif playerY > self.rowLen*3 and playerY < self.rowLen * 4:
                self.currRow = 3

    ########################################
    # Display's count of monsters in house
    ########################################
    def homeData(self, playerX, playerY):
        msg = ""
        color = (0, 0, 0)
        home = self.controller.neighborhood.houseList[self.currRow][self.currCol]
        numMonsters = home.monstersRem
        if numMonsters == 0:
            msg = "SAFE!"
            color = self.green
        else:
            msg = repr(numMonsters) + " MONSTERS!"
            color = self.red
        x = playerX - 50
        y = playerY - 50
        self.displayData(msg, color, x, y)

    ####################################
    # Display's monsters when fighting
    ####################################
    def displayMonsters(self):
        monsters = self.currentHouse.monsters
        monsterSpacing = 120
        monsterX = 0
        monsterY = 400

        for monster in monsters:
            if monster.monType == "zombie":
                self.screen.blit(self.zombie, (monsterX, monsterY))
            elif monster.monType == "ghoul":
                self.screen.blit(self.ghoul, (monsterX, monsterY))
            elif monster.monType == "vampire":
                self.screen.blit(self.vampire, (monsterX, monsterY))
            elif monster.monType == "werewolf":
                self.screen.blit(self.werewolf, (monsterX, monsterY))
            elif monster.monType == "person":
                self.screen.blit(self.person, (monsterX, monsterY))
            monsterX += monsterSpacing

    #############################
    # Display's current weapons
    #############################
    def printWeapons(self):
        width = 20
        height = 20
        widthSpacing = 280
        heightSpacing = 30
        itemIndex = 0

        items = self.controller.playerOne.stock

        for item in items:
            self.displayData("" + repr(itemIndex) + ": " + item.weapType + " x " + repr(item.ammo) + " uses left", self.lightblue, width, height)
            width += widthSpacing
            itemIndex += 1
            if width > 800:
                width = 20
                height += heightSpacing

    ######################################################
    # Establishes a cell size for each house on the grid
    ######################################################
    def genGrid(self):

        self.nMap = [[[200, 300], [400, 300], [600, 300]],
                         [[200, 600], [400, 600], [600, 600]],
                         [[200, 900], [400, 900], [600, 900]]
                         ]

        self.colLen = 300
        self.rowLen = 200
        self.currRow = 0
        self.currCol = 0
        self.currentHouse = self.controller.neighborhood.houseList[self.currRow][self.currCol]

    ##################################################
    # Helper method that generates all of the images
    ##################################################
    def genImages(self):

        # Backgrounds
        self.bg = self.getImage('assets/neighborhood.png')
        self.battleBG = self.getImage('assets/battlefieldP.png')

        # Text
        self.font = pygame.font.SysFont("Comic Sans MS", 18)

        # Monsters
        self.zombie = self.getImage('assets/zombie.jpg')
        self.ghoul = self.getImage('assets/ghoul.jpg')
        self.vampire = self.getImage('assets/vampire.jpg')
        self.person = self.getImage('assets/person.jpg')
        self.werewolf = self.getImage('assets/werewolf.jpg')

    ##############################################
    # Helper function that creates useful colors
    ##############################################
    def createColor(self):
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.lightblue = (135, 206, 250)

    ############################################
    # Handles all of the logic during battle
    ############################################
    def fight(self, weapon):
        screenText = True
        fightDialogue = []
        fightDialogueIndex = 0
        winFight = False
        self.screen.fill(self.black)
        self.screen.blit(self.battleBG, (0, 200))
        self.screen.fill(self.white, rect=[650, 700, 10, 250])
        self.screen.fill(self.white, rect=[650, 700, 250, 10])
        self.screen.fill(self.white, rect=[900, 700, 10, 250])
        self.screen.fill(self.lightblue, rect=[660, 710, 240, 240])
        self.displayData("Zork", self.white, 680, 730)
        self.displayData("HP: " + repr(self.controller.playerOne.playerHP
                                         ), self.white, 680, 790)
        self.displayData("You used: " + weapon.weapType, self.green, 20, 20)
        self.displayMonsters()

        monsters = self.currentHouse.monsters
        player = self.controller.playerOne

        for monster in monsters:
            name = monster.monType
            info = monster.mHit(player.pAttack(weapon))

            fightDialogue.append(repr(info["damage"]) + "HP damage to " + name)
            if info['dead']:
                fightDialogue.append(name + " has turned back into a person!")
        for monster in monsters:
            player.pHit(monster.mAttacking())
            fightDialogue.append(monster.monType + " attacked and dealt " + repr(monster.attDamage) + " damage!")
        if player.playerHP\
                <= 0:
            fightDialogue.append("You died!!")
        if self.currentHouse.monstersRem == 0:
            fightDialogue.append("The house has been cleared!")
            winFight = True

        pygame.display.update()
        while screenText:
            self.screen.fill(self.black)
            self.screen.blit(self.battleBG, (0, 200))
            self.screen.fill(self.white, rect=[650, 700, 10, 250])
            self.screen.fill(self.white, rect=[650, 700, 250, 10])
            self.screen.fill(self.white, rect=[900, 700, 10, 250])
            self.screen.fill(self.lightblue, rect=[660, 710, 240, 240])
            self.displayData("Zork ", self.white, 680, 730)
            self.displayData("HP: " + repr(self.controller.playerOne.playerHP
                                             ), self.white, 680, 790)
            self.displayMonsters()


            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if fightDialogueIndex < len(fightDialogue):
                            self.displayData(fightDialogue[fightDialogueIndex], self.white, 20, 20)
                            fightDialogueIndex += 1
                            pygame.display.update()
                        elif player.playerHP <= 0:
                            self.gameOver = True
                            isFighting = False
                            self.run()
                        else:
                            screenText = False
        if winFight:
            self.isFighting = False
            self.onController = True
            pygame.display.update()
            self.run()
            

##############################################
#Main Method class starts the entire program
##############################################


class MainMethod:
    if __name__ == '__main__':
        g = Game()
        g.run()
