from world_classes.Animal import Animal
from world_classes.Point import Point


class Person(Animal):

    def __init__(self, position, Settings):
        self.Settings = Settings
        self.symbol = self.Settings.symbol_person
        self.power = self.Settings.power_person
        self.initiative = self.Settings.initiative_person
        self.color = self.Settings.color_person
        self.__next_move = None
        super().__init__(self.symbol, self.power, self.initiative, self.color, position)

    def power_p(self):
        

    def get_next_move(self):
        if self.__next_move:
            if self.Settings is None:
                a = 10
            new_point = Point(self.position.x, self.position.y, self.Settings)
            if self.__next_move[1] == 'x':
                new_point.offset(self.__next_move[0], 0)
            else:
                new_point.offset(0, self.__next_move[0])
            return new_point
        return None

    def set_next_move(self, pointTo, step=1):
        if pointTo == 0:
            self.__next_move = [step, 'y']
        elif pointTo == 1:
            self.__next_move = [-step, 'x']
        elif pointTo == 2:
            self.__next_move = [-step, 'y']
        elif pointTo == 3:
            self.__next_move = [step, 'x']
        else:
            self.__next_move = None

    def action(self, objects):
        next_point = self.get_next_move()
        if next_point is None:
            return
        if objects[next_point.x][next_point.y] is not None:
            if objects[self.position.x][self.position.y].power < objects[next_point.x][next_point.y].power:
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
        print(objects[next_point.x][next_point.y].power)