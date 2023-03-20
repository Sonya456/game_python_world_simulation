from world_classes.Plant import Plant
import random

from world_classes.Point import Point


class Barszcz(Plant):
    def __init__(self, position, Settings):
        self.Settings = Settings
        self.symbol = self.Settings.symbol_barszczy
        self.power = self.Settings.power_barszczy
        self.color = self.Settings.color_barszczy
        super().__init__(self.symbol, self.power, self.color, position)

    def get_next_move(self):
        next_side = Point.get_random_side()
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
        self.action_barszcz(objects, self.position.x, self.position.y)
        next_point = self.get_next_move()
        if objects[next_point.x][next_point.y] is not None or random.randint(0, 10) > 2 or self.Settings.max_count_trawy < 0:
            if objects[self.position.x][self.position.y] is not None:
                objects[self.position.x][self.position.y].set_can_move(False)
        else:
            self.kill(objects, next_point)

    def kill(self, objects, next_point):
        if objects[self.position.x][self.position.y] is not None:
            objects[next_point.x][next_point.y] = objects[self.position.x][self.position.y]
            objects[next_point.x][next_point.y].set_position(next_point)
            objects[next_point.x][next_point.y].set_can_move(False)
            self.Settings.max_count_trawy -= 1
            objects[next_point.x][next_point.y].age = 0

    def action_barszcz(self, objects, del_x, del_y):
        if del_x - 1 >= 0 and del_y - 1 >= 0 and objects[del_x - 1][del_y - 1] is not None and objects[del_x - 1][
            del_y - 1].get_symbol() != self.Settings.symbol_barszczy and objects[del_x - 1][
            del_y - 1].get_symbol() != self.Settings.symbol_cyber_owcy:
            objects[del_x - 1][del_y - 1] = None
        if del_x - 1 >= 0 and objects[del_x - 1][del_y] is not None and objects[del_x - 1][
            del_y].get_symbol() != self.Settings.symbol_barszczy and objects[del_x - 1][
            del_y].get_symbol() != self.Settings.symbol_cyber_owcy:
            objects[del_x - 1][del_y] = None
        if del_y - 1 >= 0 and objects[del_x][del_y - 1] is not None and objects[del_x][
            del_y - 1].get_symbol() != self.Settings.symbol_barszczy and objects[del_x][
            del_y - 1].get_symbol() != self.Settings.symbol_cyber_owcy:
            objects[del_x][del_y - 1] = None
        if del_x + 1 < self.Settings.world_size and del_y + 1 < self.Settings.world_size and objects[del_x + 1][del_y + 1] is not None and objects[del_x + 1][
            del_y + 1].get_symbol() != self.Settings.symbol_barszczy and objects[del_x + 1][
            del_y + 1].get_symbol() != self.Settings.symbol_cyber_owcy:
            objects[del_x + 1][del_y + 1] = None
        if del_y - 1 >= 0 and del_x + 1 < self.Settings.world_size and objects[del_x + 1][del_y - 1] is not None and objects[del_x + 1][
            del_y - 1].get_symbol() != self.Settings.symbol_barszczy and objects[del_x + 1][
            del_y - 1].get_symbol() != self.Settings.symbol_cyber_owcy:
            objects[del_x + 1][del_y - 1] = None
        if del_x - 1 >= 0 and del_y + 1 < self.Settings.world_size and objects[del_x - 1][del_y + 1] is not None and objects[del_x - 1][
            del_y + 1].get_symbol() != self.Settings.symbol_barszczy and objects[del_x - 1][
            del_y + 1].get_symbol() != self.Settings.symbol_cyber_owcy:
            objects[del_x - 1][del_y + 1] = None
        if del_y + 1 < self.Settings.world_size and objects[del_x][del_y + 1] is not None and objects[del_x][
            del_y + 1].get_symbol() != self.Settings.symbol_barszczy and objects[del_x][
            del_y + 1].get_symbol() != self.Settings.symbol_cyber_owcy:
            objects[del_x][del_y + 1] = None
        if del_x + 1 < self.Settings.world_size and objects[del_x + 1][del_y] is not None and objects[del_x + 1][
            del_y].get_symbol() != self.Settings.symbol_barszczy and objects[del_x + 1][
            del_y].get_symbol() != self.Settings.symbol_cyber_owcy:
            objects[del_x + 1][del_y] = None
