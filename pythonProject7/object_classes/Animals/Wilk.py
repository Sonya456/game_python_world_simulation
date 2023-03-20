from world_classes.Animal import Animal
from world_classes.Point import Point


class Wilk(Animal):
    def __init__(self, position, Settings):
        self.Settings = Settings
        self.symbol = self.Settings.symbol_wilka
        self.power = self.Settings.power_wilka
        self.initiative = self.Settings.initiative_wilka
        self.color = self.Settings.color_wilka

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
        if objects[next_point.x][next_point.y] is not None:
            if objects[next_point.x][next_point.y].get_symbol() == self.Settings.symbol_wilka:
                self.add(objects, next_point)
                next_point = self.get_next_move()
                self.add(objects, next_point)
            elif objects[self.position.x][self.position.y].power < objects[next_point.x][next_point.y].power:
                objects[self.position.x][self.position.y] = None
            else:
                self.kill(objects, next_point)
        else:
            self.kill(objects, next_point)

    def kill(self, objects, next_point):
            objects[next_point.x][next_point.y] = objects[self.position.x][self.position.y]
            objects[self.position.x][self.position.y] = None
            objects[next_point.x][next_point.y].set_position(next_point)
            objects[next_point.x][next_point.y].set_can_move(False)

    def add(self, objects, next_point):
        objects[next_point.x][next_point.y] = objects[self.position.x][self.position.y]
        objects[next_point.x][next_point.y].set_position(next_point)
        objects[next_point.x][next_point.y].set_can_move(False)