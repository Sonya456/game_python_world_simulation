class Settings:
    # main


    def __init__(self, world_size=20):
        self.__default_color = 'white'
        self.__color_wilka = 'grey'
        self.__initiative_wilka = 5
        self.__power_wilka = 9
        self.__max_count_wilka = 10
        self.__symbol_wilka = 'W'

        self.__initiative_cyber_owcy = 4
        self.__power_cyber_owcy = 11
        self.__max_count_cyber_owcy = 3
        self.__symbol_cyber_owcy = 'C'
        self.__color_cyber_owcy = '#CCE5FF'

        self.__power_barszczy = 10
        self.__max_count_barszczy = 4
        self.__symbol_barszczy = '~'
        self.__color_barszczy = '#660033'

        self.__power_jagody = 99
        self.__max_count_jagody = 4
        self.__symbol_jagody = 'J'
        self.__color_jagody = '#990099'

        self.__max_count_gurany = 8
        self.__symbol_gurany = 'G'
        self.__color_gurany = '#FF3333'

        self.__max_count_mlecza = 7
        self.__symbol_mlecza = 'M'
        self.__color_mlecza = '#A2A6D5'

        self.__max_count_trawy = 40
        self.__symbol_trawy = 'T'
        self.__color_trawy = 'green'

        self.__chance_make_move_zolw = 0.25
        self.__initiative_zolw = 1
        self.__power_zolw = 2
        self.__max_count_zolw = 10
        self.__symbol_zolw = 'Z'
        self.__color_zolw = '#C0C0C0'

        self.__initiative_lisa = 7
        self.__power_lisa = 4
        self.__max_count_lisa = 15
        self.__symbol_lisa = 'L'
        self.__color_lisa = '#FF9933'

        self.__initiative_owcy = 4
        self.__symbol_owcy = 'O'
        self.__power_owcy = 4
        self.__max_count_owcy = 16
        self.__color_owcy = '#CCE5FF'

        self.__move_count_antylopy = 2
        self.__chance_for_run_antylopy = 0.5
        self.__max_count_antylopy = 7
        self.__initiative_antylopy = 4
        self.__power_antylopy = 4
        self.__symbol_antylopy = 'A'
        self.__color_antylopy = '#E5FFCC'

        self.__max_tour_to_win = 300
        self.__new = 'n'
        self.__run = 'r'
        self.__save = 'u'
        self.__load = 'l'
        self.__quite = 'q'

        self.__delay_between_tours = 0
        self.__world_size = world_size
        self.__object_count = 20

        self.__symbol_person = 'H'
        self.__power_person = 5
        self.__initiative_person = 4
        self.__color_person = '#FFCCCC'
        self.__point_x_person = None
        self.__point_y_person = None

    @property
    def default_color(self):
        return self.__default_color

    @property
    def color_person(self):
        return self.__color_person

    @color_person.setter
    def color_person(self, value):
        self.__color_person = value

    @property
    def color_antylopy(self):
        return self.__color_antylopy

    @color_antylopy.setter
    def color_antylopy(self, value):
        self.__color_antylopy = value

    @property
    def color_cyber_owcy(self):
        return self.__color_cyber_owcy

    @color_cyber_owcy.setter
    def color_cyber_owcy(self, value):
        self.__color_cyber_owcy = value

    @property
    def color_lisa(self):
        return self.__color_lisa

    @color_lisa.setter
    def color_lisa(self, value):
        self.__color_lisa = value

    @property
    def color_zolw(self):
        return self.__color_zolw

    @color_zolw.setter
    def color_zolw(self, value):
        self.__color_zolw = value

    @property
    def color_owcy(self):
        return self.__color_owcy

    @color_owcy.setter
    def color_owcy(self, value):
        self.__color_owcy = value

    @property
    def color_jagody(self):
        return self.__color_jagody

    @color_jagody.setter
    def color_gurany(self, value):
        self.__color_jagody = value

    @property
    def color_barszczy(self):
        return self.__color_barszczy

    @color_barszczy.setter
    def color_barszczy(self, value):
        self.__color_barszczy = value

    @property
    def color_gurany(self):
        return self.__color_gurany

    @color_gurany.setter
    def color_gurany(self, value):
        self.__color_gurany = value

    @property
    def color_mlecza(self):
        return self.__color_mlecza

    @color_mlecza.setter
    def color_mlecza(self, value):
        self.__color_mlecza = value

    @property
    def world_size(self):
        return self.__world_size

    @world_size.setter
    def world_size(self, value):
        self.__world_size = value

    @property
    def color_trawy(self):
        return self.__color_trawy

    @color_trawy.setter
    def color_trawy(self, value):
        self.__color_trawy = value

    @property
    def object_count(self):
        return self.__object_count

    @object_count.setter
    def object_count(self, value):
        self.__object_count = value

    # Person
    @property
    def symbol_person(self):
        return self.__symbol_person

    @symbol_person.setter
    def symbol_person(self, value):
        self.__symbol_person = value

    @property
    def power_person(self):
        return self.__power_person

    @power_person.setter
    def power_person(self, value):
        self.__power_person = value

    @property
    def initiative_person(self):
        return self.__initiative_person

    @initiative_person.setter
    def initiative_person(self, value):
        self.__initiative_person = value

    # Antylopa

    @property
    def symbol_antylopy(self):
        return self.__symbol_antylopy

    @symbol_antylopy.setter
    def symbol_antylopy(self, value):
        self.__symbol_antylopy = value

    @property
    def max_count_antylopy(self):
        return self.__max_count_antylopy

    @max_count_antylopy.setter
    def max_count_antylopy(self, value):
        self.__max_count_antylopy = value

    @property
    def power_antylopy(self):
        return self.__power_antylopy

    @power_antylopy.setter
    def power_antylopy(self, value):
        self.__power_antylopy = value

    @property
    def initiative_antylopy(self):
        return self.__initiative_antylopy

    @initiative_antylopy.setter
    def initiative_antylopy(self, value):
        self.__initiative_antylopy = value

    @property
    def chance_for_run_antylopy(self):
        return self.__chance_for_run_antylopy

    @chance_for_run_antylopy.setter
    def chance_for_run_antylopy(self, value):
        self.__chance_for_run_antylopy = value

    @property
    def move_count_antylopy(self):
        return self.__move_count_antylopy

    @move_count_antylopy.setter
    def move_count_antylopy(self, value):
        self.__move_count_antylopy = value

    # Owca

    @property
    def symbol_owcy(self):
        return self.__symbol_owcy

    @symbol_owcy.setter
    def symbol_owcy(self, value):
        self.__symbol_owcy = value

    @property
    def max_count_owcy(self):
        return self.__max_count_owcy

    @max_count_owcy.setter
    def max_count_owcy(self, value):
        self.__max_count_owcy = value

    @property
    def power_owcy(self):
        return self.__power_owcy

    @power_owcy.setter
    def power_owcy(self, value):
        self.__power_owcy = value

    @property
    def initiative_owcy(self):
        return self.__initiative_owcy

    @initiative_owcy.setter
    def initiative_owcy(self, value):
        self.__initiative_owcy = value

    # Cyber owca

    @property
    def symbol_cyber_owcy(self):
        return self.__symbol_cyber_owcy

    @symbol_cyber_owcy.setter
    def symbol_cyber_owcy(self, value):
        self.__symbol_cyber_owcy = value

    @property
    def max_count_cyber_owcy(self):
        return self.__max_count_cyber_owcy

    @max_count_cyber_owcy.setter
    def max_count_cyber_owcy(self, value):
        self.__max_count_cyber_owcy = value

    @property
    def power_cyber_owcy(self):
        return self.__power_cyber_owcy

    @power_cyber_owcy.setter
    def power_cyber_owcy(self, value):
        self.__power_cyber_owcy = value

    @property
    def initiative_cyber_owcy(self):
        return self.__initiative_cyber_owcy

    @initiative_cyber_owcy.setter
    def initiative_cyber_owcy(self, value):
        self.__initiative_cyber_owcy = value

    # Wilk
    @property
    def symbol_wilka(self):
        return self.__symbol_wilka

    @symbol_wilka.setter
    def symbol_wilka(self, value):
        self.__symbol_wilka = value

    @property
    def max_count_wilka(self):
        return self.__max_count_wilka

    @max_count_wilka.setter
    def max_count_wilka(self, value):
        self.__max_count_wilka = value

    @property
    def power_wilka(self):
        return self.__power_wilka

    @power_wilka.setter
    def power_wilka(self, value):
        self.__power_wilka = value

    @property
    def initiative_wilka(self):
        return self.__initiative_wilka

    @initiative_wilka.setter
    def initiative_wilka(self, value):
        self.__initiative_wilka = value

    @property
    def color_wilka(self):
        return self.__color_wilka

    @color_wilka.setter
    def color_wilka(self, value):
        self.__color_wilka = value

    # Lis

    @property
    def symbol_lisa(self):
        return self.__symbol_lisa

    @symbol_lisa.setter
    def symbol_lisa(self, value):
        self.__symbol_lisa = value

    @property
    def max_count_lisa(self):
        return self.__max_count_lisa

    @max_count_lisa.setter
    def max_count_lisa(self, value):
        self.__max_count_lisa = value

    @property
    def power_lisa(self):
        return self.__power_lisa

    @power_lisa.setter
    def power_lisa(self, value):
        self.__power_lisa = value

    @property
    def initiative_lisa(self):
        return self.__initiative_lisa

    @initiative_lisa.setter
    def initiative_lisa(self, value):
        self.__initiative_lisa = value

    # zolw

    @property
    def symbol_zolw(self):
        return self.__symbol_zolw

    @symbol_zolw.setter
    def symbol_zolw(self, value):
        self.__symbol_zolw = value

    @property
    def max_count_zolw(self):
        return self.__max_count_zolw

    @max_count_zolw.setter
    def max_count_zolw(self, value):
        self.__max_count_zolw = value

    @property
    def power_zolw(self):
        return self.__power_zolw

    @power_zolw.setter
    def power_zolw(self, value):
        self.__power_zolw = value

    @property
    def initiative_zolw(self):
        return self.__initiative_zolw

    @initiative_zolw.setter
    def initiative_zolw(self, value):
        self.__initiative_zolw = value

    @property
    def chance_make_move_zolw(self):
        return self.__chance_make_move_zolw

    @chance_make_move_zolw.setter
    def chance_make_move_zolw(self, value):
        self.__chance_make_move_zolw = value

    # trawa

    @property
    def symbol_trawy(self):
        return self.__symbol_trawy

    @symbol_trawy.setter
    def symbol_trawy(self, value):
        self.__symbol_trawy = value

    @property
    def max_count_trawy(self):
        return self.__max_count_trawy

    @max_count_trawy.setter
    def max_count_trawy(self, value):
        self.__max_count_trawy = value

    # Mlecz

    @property
    def symbol_mlecza(self):
        return self.__symbol_mlecza

    @symbol_mlecza.setter
    def symbol_mlecza(self, value):
        self.__symbol_mlecza = value

    @property
    def max_count_mlecza(self):
        return self.__max_count_mlecza

    @max_count_mlecza.setter
    def max_count_mlecza(self, value):
        self.__max_count_mlecza = value

    # Gurana

    @property
    def symbol_gurany(self):
        return self.__symbol_gurany

    @symbol_gurany.setter
    def symbol_gurany(self, value):
        self.__symbol_gurany = value

    @property
    def max_count_gurany(self):
        return self.__max_count_gurany

    @max_count_gurany.setter
    def max_count_gurany(self, value):
        self.__max_count_gurany = value

    # Wilcze jagody
    @property
    def symbol_jagody(self):
        return self.__symbol_jagody

    @symbol_jagody.setter
    def symbol_jagody(self, value):
        self.__symbol_jagody = value

    @property
    def max_count_jagody(self):
        return self.__max_count_jagody

    @max_count_jagody.setter
    def max_count_jagody(self, value):
        self.__max_count_jagody = value

    @property
    def power_jagody(self):
        return self.__power_jagody

    @power_jagody.setter
    def power_jagody(self, value):
        self.__power_jagody = value

    # Barszcz sosnowskiego
    @property
    def symbol_barszczy(self):
        return self.__symbol_barszczy

    @symbol_barszczy.setter
    def symbol_barszczy(self, value):
        self.__symbol_barszczy = value

    @property
    def max_count_barszczy(self):
        return self.__max_count_barszczy

    @max_count_barszczy.setter
    def max_count_barszczy(self, value):
        self.__max_count_barszczy = value

    @property
    def power_barszczy(self):
        return self.__power_barszczy

    @power_barszczy.setter
    def power_barszczy(self, value):
        self.__power_barszczy = value

    #  Game settings
    @property
    def quite(self):
        return self.__quite

    @quite.setter
    def quite(self, value):
        self.__quite = value

    @property
    def load(self):
        return self.__load

    @load.setter
    def load(self, value):
        self.__load = value

    @property
    def save(self):
        return self.__save

    @save.setter
    def save(self, value):
        self.__save = value

    @property
    def run(self):
        return self.__run

    @run.setter
    def run(self, value):
        self.__run = value

    @property
    def new(self):
        return self.__new

    @new.setter
    def new(self, value):
        self.__new = value

    @property
    def max_tour_to_win(self):
        return self.__max_tour_to_win

    @max_tour_to_win.setter
    def max_tour_to_win(self, value):
        self.__max_tour_to_win = value

    @property
    def delay_between_tours(self):
        return self.__delay_between_tours

    @delay_between_tours.setter
    def delay_between_tours(self, value):
        self.__delay_between_tours = value
