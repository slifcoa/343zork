# @author Adam Slifco
# @author Zack Hern

from random import uniform, seed

################################################
# Main weapons class and all inherited forms
################################################
class Weapon(object):

    ########################################################
    # method allows for easy way to add inherited types
    ########################################################

    # Factory concept obtained from https://pythonspot.com/en/factory-method/
    # Originally overheard about the concept (accidental eavesdrop) from students in eosLab
    # makes it easy to create new inherited subclasses
    def factory(weaponType):
        if weaponType == "chocolatebar": return ChocolateBar()
        if weaponType == "hersheykiss": return HersheyKiss()
        if weaponType == "nerdbomb": return NerdBomb()
        if weaponType == "sourstraw": return SourStraw()
        assert 0, "Invalid type: " + weaponType
    factory = staticmethod(factory)

########################################
# Inherited classes of the Weapon class.
########################################
class ChocolateBar(Weapon):
    def __init__(self):
        self.weapType = "ChocolateBar"
        seed()
        self.aModifier = uniform(2, 2.4)
        self.ammo = 4

class HersheyKiss(Weapon):
    def __init__(self):
        self.weapType = "HersheyKiss"
        self.aModifier = 1
        self.ammo = float('inf')

class NerdBomb(Weapon):
    def __init__(self):
        self.weapType = "NerdBomb"
        seed()
        self.aModifier = uniform(3.5, 5)
        self.ammo = 1

class SourStraw(Weapon):
    def __init__(self):
        self.weapType = "SourStraw"
        seed()
        self.aModifier = uniform(1, 1.75)
        self.ammo = 2

