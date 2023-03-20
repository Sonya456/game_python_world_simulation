import random
from itertools import groupby

from object_classes.Animals.Antylopa import Antylopa
from object_classes.Animals.CyberOwca import CyberOwca
from object_classes.Animals.Lis import Lis
from object_classes.Animals.Owca import Owca
from object_classes.Animals.Person import Person
from object_classes.Animals.Wilk import Wilk
from object_classes.Animals.Zolw import Zolw
from object_classes.Plants.Barszcz import Barszcz
from object_classes.Plants.Gurana import Gurana
from object_classes.Plants.Jagody import Jagody
from object_classes.Plants.Mlecz import Mlecz
from object_classes.Plants.Trawa import Trawa
from world_classes.Point import Point


class World:
    def __init__(self, Settings, buttons, objects, root):
        self.Settings = Settings
        self.buttons = buttons
        self.objects = objects
        self.population = 3
        self.root = root
        self.point_person = None
        self.initiative = []

    def add_objects(self, symbol, color, max_count):
        for _ in range(int(max_count / self.population)):
            x = random.randint(0, self.Settings.world_size - 1)
            y = random.randint(0, self.Settings.world_size - 1)
            while self.objects[x][y]:
                x = random.randint(0, self.Settings.world_size - 1)
                y = random.randint(0, self.Settings.world_size - 1)
            # self.buttons[x][y]['text'] = symbol
            # self.buttons[x][y]['bg'] = color
            if symbol == self.Settings.symbol_person:
                self.objects[x][y] = Person(Point(x, y, self.Settings), self.Settings)
            elif symbol == self.Settings.symbol_antylopy:
                self.objects[x][y] = Antylopa(Point(x, y, self.Settings), self.Settings)
            elif symbol == self.Settings.symbol_barszczy:
                self.objects[x][y] = Barszcz(Point(x, y, self.Settings), self.Settings)
            elif symbol == self.Settings.symbol_trawy:
                self.objects[x][y] = Trawa(Point(x, y, self.Settings), self.Settings)
            elif symbol == self.Settings.symbol_jagody:
                self.objects[x][y] = Jagody(Point(x, y, self.Settings), self.Settings)
            elif symbol == self.Settings.symbol_owcy:
                self.objects[x][y] = Owca(Point(x, y, self.Settings), self.Settings)
            elif symbol == self.Settings.symbol_cyber_owcy:
                self.objects[x][y] = CyberOwca(Point(x, y, self.Settings), self.Settings)
            elif symbol == self.Settings.symbol_lisa:
                self.objects[x][y] = Lis(Point(x, y, self.Settings), self.Settings)
            elif symbol == self.Settings.symbol_wilka:
                self.objects[x][y] = Wilk(Point(x, y, self.Settings), self.Settings)
            elif symbol == self.Settings.symbol_zolw:
                self.objects[x][y] = Zolw(Point(x, y, self.Settings), self.Settings)
            elif symbol == self.Settings.symbol_gurany:
                self.objects[x][y] = Gurana(Point(x, y, self.Settings), self.Settings)
            elif symbol == self.Settings.symbol_mlecza:
                self.objects[x][y] = Mlecz(Point(x, y, self.Settings), self.Settings)
            self.objects[x][y].set_position(Point(x, y, self.Settings))
        self.objects[x][y].age = 0
        self.draw()


    def run(self):

        self.root.bind("<space>", lambda event: self.initiative_organism(-1))
        self.root.bind("<s>", lambda event: self.initiative_organism(3))
        self.root.bind("<a>", lambda event: self.initiative_organism(2))
        self.root.bind("<w>", lambda event: self.initiative_organism(1))
        self.root.bind("<d>", lambda event: self.initiative_organism(0))

    def next_tour(self, pointTo, element):
        self.Settings.delay_between_tours += 1
        for y in range(self.Settings.world_size):
            for x in range(self.Settings.world_size):
                if self.objects[x][y] is not None and self.objects[x][y].get_can_move() and self.objects[x][y].initiative*1000 + self.objects[x][y].age == element:
                    self.objects[x][y].age += 1
                    if self.objects[x][y].get_symbol() == self.Settings.symbol_person:
                        self.objects[x][y].set_next_move(pointTo)
                    self.objects[x][y].action(self.objects)
        self.draw()
        #self.initiative_organism()

    def initiative_organism(self, pointTo):
        for x in range(self.Settings.world_size*self.Settings.world_size):
            self.initiative.append(0)
        z = 0
        for y in range(self.Settings.world_size):
            for x in range(self.Settings.world_size):
                if self.objects[x][y] is not None:
                    self.initiative[z] = self.objects[x][y].initiative*1000 + self.objects[x][y].age
                    z += 1
        self.initiative.sort(reverse=True)
        new_initiative = [el for el, _ in groupby(self.initiative)]
        # print(new_initiative)
        for element in new_initiative:
            # print(element)
            self.next_tour(pointTo, element)


    def plant_or_animals(self, objects, x, y):
        if (objects[x][y].get_symbol() == self.Settings.symbol_trawy or objects[x][y].get_symbol() == self.Settings.symbol_gurany
        or objects[x][y].get_symbol() == self.Settings.symbol_barszczy or objects[x][y].get_symbol() == self.Settings.symbol_jagody
        or objects[x][y].get_symbol() == self.Settings.symbol_mlecza):
            return False
        else:
            return True



    def load_world(self, loaded=None):
        if loaded:
            pass
        else:
            for x in range(self.Settings.world_size):
                self.objects.append([])
                for y in range(self.Settings.world_size):
                    self.objects[x].append(None)
            self.add_objects(self.Settings.symbol_trawy, self.Settings.color_trawy, self.Settings.max_count_trawy)
            self.add_objects(self.Settings.symbol_mlecza, self.Settings.color_mlecza, self.Settings.max_count_mlecza)
            self.add_objects(self.Settings.symbol_gurany, self.Settings.color_gurany, self.Settings.max_count_gurany)
            self.add_objects(self.Settings.symbol_jagody, self.Settings.color_jagody, self.Settings.max_count_jagody)
            self.add_objects(self.Settings.symbol_barszczy, self.Settings.color_barszczy, self.Settings.max_count_barszczy)

            self.add_objects(self.Settings.symbol_lisa, self.Settings.color_lisa, self.Settings.max_count_lisa)
            self.add_objects(self.Settings.symbol_cyber_owcy, self.Settings.color_cyber_owcy, self.Settings.max_count_cyber_owcy)
            self.add_objects(self.Settings.symbol_owcy, self.Settings.color_owcy, self.Settings.max_count_owcy)
            self.add_objects(self.Settings.symbol_zolw, self.Settings.color_zolw, self.Settings.max_count_zolw)
            self.add_objects(self.Settings.symbol_wilka, self.Settings.color_wilka, self.Settings.max_count_wilka)
            self.add_objects(self.Settings.symbol_antylopy, self.Settings.color_antylopy, self.Settings.max_count_antylopy)
            self.add_objects(self.Settings.symbol_person, self.Settings.color_person, self.population)

    def draw(self):
        for i, x in enumerate(range(self.Settings.world_size)):
            for k, y in enumerate(range(self.Settings.world_size)):
                if self.objects[x][y]:
                    self.objects[x][y].set_can_move(True)
                    self.buttons[x][y]['text'] = self.objects[x][y].get_symbol()
                    self.buttons[x][y]['bg'] = self.objects[x][y].get_color()
                else:
                    self.buttons[x][y]['text'] = ' '
                    self.buttons[x][y]['bg'] = self.Settings.default_color

    # def point(self):
    # def run_animals(self, point):
    #     organism = Organism()
    #     self.draw.run_person(point, self.Settings.symbol_lisa, self.Settings.color_lisa, self.Settings.power_lisa)
    #     self.draw.run_person(point, self.Settings.symbol_wilka, self.Settings.color_wilka, self.Settings.power_wilka)
    #     self.draw.run_person(point, self.Settings.symbol_antylopy, self.Settings.color_antylopy, self.Settings.power_antylopy)
    #     self.draw.run_person(point, self.Settings.symbol_cyber_owcy, self.Settings.color_cyber_owcy, self.Settings.power_cyber_owcy)
    #     self.draw.run_person(point, self.Settings.symbol_owcy, self.Settings.color_owcy, self.Settings.power_owcy)
    #     self.draw.run_person(point, self.Settings.symbol_person, self.Settings.color_person, self.Settings.power_person)
    #     self.draw.run_person(point, self.Settings.symbol_zolw, self.Settings.color_zolw, self.Settings.power_zolw)
