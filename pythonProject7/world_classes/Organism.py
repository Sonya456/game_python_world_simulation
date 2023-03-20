from abc import abstractmethod
# from tkinter import *
# from tkinter import messagebox
# from world_classes.World import World
# import threading
# import asyncio
# import time
import random
import abc


class Organism:
    __metaclass__ = abc.ABCMeta

    def __init__(self, symbol, power, color, position, initiative=0):
        self.power = power
        self.alive = True
        self.symbol = symbol
        self.color = color
        self.position = position
        self.can_move = True
        self.age = 0
        self.initiative = initiative

    # @property
    # def power(self):
    #     return self._power
    #
    # @power.setter
    # def power(self, value):
    #     self._power = value

    @property
    def initiative(self):
        return self._initiative

    @initiative.setter
    def initiative(self, value):
        self._initiative = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @abc.abstractmethod
    def get_can_move(self):
        return self.can_move

    @abc.abstractmethod
    def set_can_move(self, value):
        self.can_move = value

    @abc.abstractmethod
    def action(self, objects):
        pass

    @abc.abstractmethod
    def get_position(self):
        return self.position

    @abc.abstractmethod
    def set_position(self, new_position):
        self.position = new_position

    @abc.abstractmethod
    def get_symbol(self):
        return self.symbol

    @abc.abstractmethod
    def get_color(self):
        return self.color

    @abc.abstractmethod
    def collision(self, organism):
        pass

    @abc.abstractmethod
    def is_alive(self):
        """returning is alive"""
        return self.alive





