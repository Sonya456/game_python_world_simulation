from random import randint

class Point:

    def __init__(self, x, y, Settings):
        self.__x = x
        self.__y = y
        self.Settings = Settings

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    def offset(self, x, y):
        self.x += x
        self.y += y

        if self.x > 0 and self.x >= self.Settings.world_size:
            self.x -= self.Settings.world_size
        elif self.x < 0:
            self.x += self.Settings.world_size

        if self.y > 0 and self.y >= self.Settings.world_size:
            self.y -= self.Settings.world_size
        elif self.y < 0:
            self.y += self.Settings.world_size

    @staticmethod
    def get_random_side():
        return randint(0, 3)

