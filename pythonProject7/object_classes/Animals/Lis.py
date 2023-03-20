from world_classes.Animal import Animal
from world_classes.Point import Point


class Lis(Animal):
    def __init__(self, position, Settings):
        self.Settings = Settings
        self.symbol = self.Settings.symbol_lisa
        self.power = self.Settings.power_lisa
        self.initiative = self.Settings.initiative_lisa
        self.color = self.Settings.color_lisa

        super().__init__(self.symbol, self.power, self.initiative, self.color, position)

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
        self.action_lis(objects, next_point)
        if objects[next_point.x][next_point.y] is not None:
            if objects[next_point.x][next_point.y].get_symbol() == self.Settings.symbol_lisa:
                self.add(objects, next_point)
            elif objects[next_point.x][next_point.y].power > self.power:
                # print(objects[next_point.x][next_point.y].power)
                next_point = self.get_next_move()
        elif objects[next_point.x][next_point.y] is not None:
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

    def action_lis(self, objects, next_point):
        while objects[next_point.x][next_point.y] is not None and objects[next_point.x][next_point.y].power > self.power and k > 0:
            next_point = self.get_next_move()
        return next_point

    def add(self, objects, next_point):
        objects[next_point.x][next_point.y] = objects[self.position.x][self.position.y]
        objects[next_point.x][next_point.y].set_position(next_point)
        objects[next_point.x][next_point.y].set_can_move(False)
