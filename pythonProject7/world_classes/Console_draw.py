from random import random

from Settings import Settings
from tkinter import *
import random

from world_classes.Animal import Animal


class Draw:
    def __init__(self, Settings, buttons, objects, root):
        self.root = root
        self.die_ob = None
        self.root = None
        self.Settings = Settings
        self.buttons = buttons
        self.objects = objects

    def run_person(self, point, symbol, color, power):
        for i, x in enumerate(range(self.Settings.world_size)):
            for k, y in enumerate(range(self.Settings.world_size)):
                self.objects[x][y] = 0

        self.Settings.delay_between_tours += 1

        for i, x in enumerate(range(self.Settings.world_size)):
            for k, y in enumerate(range(self.Settings.world_size)):
                if self.buttons[x][y]['text'] == symbol and self.objects[x][y] == 0:
                    if self.buttons[x][y]['text'] != self.Settings.symbol_person and point != -2:
                        point = random.randint(0, 3)
                    if point == 0:
                        self.run(x, y, x + 1, y, color, symbol, power)
                    if point == 1:
                        self.run(x, y, x, y - 1, color, symbol, power)
                    if point == 2:
                        self.run(x, y, x - 1, y, color, symbol, power)
                    if point == 3:
                        self.run(x, y, x, y + 1, color, symbol, power)
                    if point == -2:
                        return


    def run(self, x, y, x_1, y_1, color, symbol, power):
        if y_1 > 19: y_1 = 0
        if x_1 < 0: x_1 = 19
        if y_1 < 0: y_1 = 19
        if x_1 > 19: x_1 = 0
        if self.buttons[x_1][y_1]['text'] != " ":
            if power <= self.obj(self.buttons[x_1][y_1]['text']):
                self.die_ob = self.buttons[x][y]['text']
                self.buttons[x][y]['text'] = " "
                self.buttons[x][y]['bg'] = 'white'
                self.objects[x][y] = -1

            else:
                self.die_ob = self.buttons[x_1][y_1]['text']
                self.tura(x, y, x_1, y_1, color, symbol)
            self.print_die_obj()

        else:
            self.tura(x, y, x_1, y_1, color, symbol)

    def tura(self, x, y, x_1, y_1, color, symbol):
        self.objects[x][y] = -1
        self.buttons[x_1][y_1]['bg'] = color
        self.buttons[x_1][y_1]['text'] = symbol
        self.objects[x_1][y_1] = -1
        self.die_ob = self.buttons[x][y]['text']
        self.buttons[x][y]['text'] = " "
        self.buttons[x][y]['bg'] = 'white'
        self.objects[x][y] = -1


    def obj(self, symbol):
        if symbol == self.Settings.symbol_owcy:
            return self.Settings.power_owcy
        elif symbol == self.Settings.symbol_cyber_owcy:
            return self.Settings.power_cyber_owcy
        elif symbol == self.Settings.symbol_lisa:
            return self.Settings.power_lisa
        elif symbol == self.Settings.symbol_antylopy:
            return self.Settings.power_antylopy
        elif symbol == self.Settings.symbol_wilka:
            return self.Settings.power_wilka
        elif symbol == self.Settings.symbol_zolw:
            return self.Settings.power_zolw
        elif symbol == self.Settings.symbol_person:
            return self.Settings.power_person
        elif symbol == self.Settings.symbol_jagody:
            return 99
        elif symbol == self.Settings.symbol_barszczy:
            return 10
        else:
            return 0

    def print_die_obj(self):
        text = "object " + self.die_ob + " die"
        print(text)
        #return self.die_ob


