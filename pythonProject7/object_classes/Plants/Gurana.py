import random

from world_classes.Plant import Plant
from world_classes.Point import Point


class Gurana(Plant):
    def __init__(self, position, Settings):
        self.Settings = Settings
        self.symbol = self.Settings.symbol_gurany
        self.power = 0
        self.color = self.Settings.color_gurany
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

