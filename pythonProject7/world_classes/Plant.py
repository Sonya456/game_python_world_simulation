from world_classes.Organism import Organism
# from object_classes.Plants.Barszcz import Barszcz
# from object_classes.Plants.Mlecz import Mlecz
# from object_classes.Plants.Trawa import Trawa
# from object_classes.Plants.Gurana import Gurana
# from object_classes.Plants.Jagody import Jagody


class Plant(Organism):
    def __init__(self,symbol, power, color, position):
        super().__init__(symbol, power, color, position)
