# @author Adam Slifco
# @author Zack Hern

class Observable:

    ####################################
    # Initializes observers list
    ####################################
    def __init__(self):
        self.observers = []

    #########################################
    # Adds observer to list
    #########################################
    def addObserver(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)

    #######################################
    # Removes observer from list
    #######################################
    def removeObserver(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    ######################################
    # Completely erases observer list
    ######################################
    def removeAllObserver(self, observer):
        self.observers = []

    #################################################
    # Updates the list of observers when invoked
    #################################################
    def update(self, observed):
        for observer in self.observers:
            observer.update(observed)

