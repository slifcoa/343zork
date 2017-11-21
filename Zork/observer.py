# @author Adam Slifco
# @author Zack Hern

from abc import ABCMeta, abstractmethod

################################################
# Abstract base class for Observer pattern.
################################################
class Observer(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self):
        pass



