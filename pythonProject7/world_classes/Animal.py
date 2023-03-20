import random

from world_classes.Organism import Organism
import abc


class Animal(Organism):
    __metaclass__ = abc.ABCMeta

    def __init__(self, symbol, power, initiative, color, position):
        super().__init__(symbol, power, color, position, initiative)
        self.__current_tour = 0
        self.rand = random.randint(0, 3)


    @abc.abstractmethod
    def getNewLocation(self):
        return

    # @abc.abstractmethod
    # def get_next_move(self):
    #     return

    @property
    def current_tour(self):
        return self.__current_tour

    @current_tour.setter
    def current_tour(self, value):
        self.__current_tour = value


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

