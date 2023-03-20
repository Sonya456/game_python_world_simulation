import asyncio
import threading
from tkinter import *
from tkinter import messagebox

from object_classes.Animals.Person import Person
from world_classes.Console_draw import Draw
from world_classes.World import World
from world_classes.Animal import Animal

from Settings import Settings


class Game:
    def __init__(self):
        self.draw = None
        self.Settings = None
        self.root = None
        self.input_size = None
        self.point = -1
        self.objects = []

    def _asyncio_thread(self, async_loop, func, params=None):
        if params:
            async_loop.run_until_complete(func(params))
        else:
            async_loop.run_until_complete(func())

    def create_new_thread(self, func, params=None):
        async_loop_func = asyncio.new_event_loop()
        asyncio.set_event_loop(async_loop_func)
        self.do_tasks(async_loop_func, func, params)

    def do_tasks(self, async_loop, func, params=None):
        """ Button-Event-Handler starting the asyncio part. """
        threading.Thread(target=self._asyncio_thread, args=(async_loop, func, params)).start()

    async def close_enter_window(self):

        if self.input_size.get().isnumeric():
            self.root.destroy()
        else:
            messagebox.showwarning("Creating new world", "Your input is incorrect!")

    async def onButtonClicked2(self):
        print("New window!!")
        # print(message.get())

    def start_game(self):
        self.Settings = Settings(world_size=int(self.input_size.get()))
        t = 30 * self.Settings.world_size
        y = 26 * self.Settings.world_size

        self.root = Tk()
        self.root.title('183052')
        print(str(int(t)) + 'x' + str(int(y)) + '+700+200')
        self.root.geometry(str(int(t)) + 'x' + str(int(y)) + '+700+200')

        btn_dict = []
        for i, x in enumerate(range(self.Settings.world_size)):
            btn_dict.append({})
            for k, y in enumerate(range(self.Settings.world_size)):
                btn_dict[i][k] = Button(self.root, text=" ", bg='white',
                                        command=lambda: self.create_new_thread(self.onButtonClicked2),
                                        width=int(self.Settings.world_size / (self.Settings.world_size / 2)),
                                        height=int(self.Settings.world_size / self.Settings.world_size))
                btn_dict[i][k].grid(row=i, column=k)
        world = World(self.Settings, btn_dict, self.objects, self.root)
        # draw = Draw(self.Settings, btn_dict, self.objects, self.root)
        # animal = Animal(draw, self.Settings)
        # person = Person(self.root, draw)
        world.load_world()
        world.run()

        # def fun(event):
        #     print('Нажата клавиша пробел')
        #
        # self.root.bind("<space>", fun)

        # person.klawa()

        self.root.mainloop()

    def start(self):

        self.root = Tk()
        self.root.title('183052')
        self.root.geometry('300x35+700+200')

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.input_size = StringVar()
        size_entry = Entry(textvariable=self.input_size, bg='#CCFFFF', bd=3)
        size_entry.grid(column=0, row=0, sticky=W)
        but = Button(self.root, text="New Game", command=lambda: self.create_new_thread(self.close_enter_window))
        but.grid(column=1, row=0, sticky=W)
        but_1 = Button(self.root, text="Load Game", command=lambda: self.create_new_thread(self.close_enter_window))
        but_1.grid(column=2, row=0, sticky=W)

        self.root.mainloop()
        self.start_game()
