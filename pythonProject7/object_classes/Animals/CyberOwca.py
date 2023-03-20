from world_classes.Animal import Animal
import random

from world_classes.Point import Point


class CyberOwca(Animal):
    def __init__(self, position, Settings):
        self.Settings = Settings
        self.symbol = self.Settings.symbol_cyber_owcy
        self.power = self.Settings.power_cyber_owcy
        self.initiative = self.Settings.initiative_cyber_owcy
        self.color = self.Settings.color_cyber_owcy

        super().__init__(self.symbol, self.power, self.initiative, self.color, position)

    def get_next_move(self, objects):
        next_side = self.action_cyber_owca(objects)
        new_point = Point(self.position.x, self.position.y, self.Settings)
        if next_side == 0:
            new_point.offset(0, 1)
        elif next_side == 1:
            new_point.offset(-1, 0)
        elif next_side == 2:
            new_point.offset(0, -1)
        elif next_side == 3:
            new_point.offset(1, 0)
        return new_point

    def action(self, objects):
        next_point = self.get_next_move(objects)
        if objects[next_point.x][next_point.y] is not None:
            if objects[next_point.x][next_point.y].get_symbol() == self.Settings.symbol_cyber_owcy:
                self.add(objects, next_point)
                next_point = self.get_next_move(objects)
                self.add(objects, next_point)
            elif objects[self.position.x][self.position.y].power < objects[next_point.x][next_point.y].power:
                objects[self.position.x][self.position.y] = None
            else:
                if objects[next_point.x][next_point.y].get_symbol() == self.Settings.symbol_gurany:
                    objects[self.position.x][self.position.y].power += 3
                self.kill(objects, next_point)
        else:
            self.kill(objects, next_point)

    def kill(self, objects, next_point):
        objects[next_point.x][next_point.y] = objects[self.position.x][self.position.y]
        objects[self.position.x][self.position.y] = None
        objects[next_point.x][next_point.y].set_position(next_point)
        objects[next_point.x][next_point.y].set_can_move(False)

    def action_cyber_owca(self, objects):
        cel_x = None
        cel_y = None
        for y in range(self.Settings.world_size):
            for x in range(self.Settings.world_size):
                if objects[x][y] is not None:
                    if objects[x][y].get_symbol() == self.Settings.symbol_barszczy:
                        if cel_x is None:
                            cel_x = x
                            cel_y = y
                        else:
                            distanse_1 = abs(self.position.x - cel_x + self.position.y - cel_y)
                            distanse_2 = abs(self.position.x - x + self.position.y - y)
                            if distanse_1 > distanse_2:
                                cel_x = x
                                cel_y = y
        if cel_x is None:
            for y in range(self.Settings.world_size):
                for x in range(self.Settings.world_size):
                    if objects[x][y] is not None:
                        if objects[x][y].get_symbol() == self.Settings.symbol_owcy:
                            if cel_x is None:
                                cel_x = x
                                cel_y = y
                            else:
                                distanse_1 = abs(self.position.x - cel_x + self.position.y - cel_y)
                                distanse_2 = abs(self.position.x - x + self.position.y - y)
                                if distanse_1 > distanse_2:
                                    cel_x = x
                                    cel_y = y
        # else:
        #     return Point.get_random_side()
        if cel_x is not None and self.position.x - cel_x < 0:
            return 3
        elif cel_x is not None and self.position.x - cel_x > 0:
            return 1
        elif cel_x is not None and self.position.x - cel_x == 0:
            if self.position.y - cel_y < 0:
                return 0
            if self.position.y - cel_y > 0:
                return 2
        else:
            return Point.get_random_side()

    def add(self, objects, next_point):
        objects[next_point.x][next_point.y] = objects[self.position.x][self.position.y]
        objects[next_point.x][next_point.y].set_position(next_point)
        objects[next_point.x][next_point.y].set_can_move(False)