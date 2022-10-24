from tkinter import FLAT, Listbox
from . import *


class Search:
    def __init__(self, parent):
        self.parent = parent
 
        self._rendered = False
        self.current_state = 0      # 0 represent hidden and 1 represent rendered

        # print(parent.winfo_y())

    def insert(self, text, cmd, *param):
        if not self._rendered:
            raise Exception("Must render the parent before calling this method")

        Button(self.container, text=text, command=lambda: cmd(*param), bd=1, pady=0, width=17, bg="white", fg="black", relief=FLAT).pack(side=TOP, fill=X)


    def prepare_obj(self):
        self.main_frame = Frame(self.parent, bg="white", height=20)

        self.container = Listbox(self.main_frame)
        self.y_scroll = Scrollbar(self.main_frame, orient=VERTICAL, command=self.container.yview)


        self.container.config(yscrollcommand=self.y_scroll.set)


    def switch_off(self):
        if self.current_state == 0:
            return

        self.current_state = 0
        self.main_frame.destroy()


    def switch_on(self):
        if self.current_state == 1:
            return

        self.current_state = 1
        self.render()
        self.main_frame.place(x=140, y=232)


    def render(self):
        self.prepare_obj()


        self.container.pack(side=LEFT, fill=BOTH, expand=True)
        self.y_scroll.pack(side=LEFT, fill=Y)

        # Button(self.container, text="hekll", width=17, pady=0, bd=1, bg="white", fg="black", relief=FLAT).pack(anchor='center', fill=X)
        self._rendered = True


