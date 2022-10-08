from . import *


class Search:
    def __init__(self, parent):
        self.parent = parent
    
        self._rendered = False

    def _gen_btn(self, text, cmd):
        if not self._rendered:
            raise Exception("Must render before calling this method")

        Button(self.main_frame, text=text, command=cmd).pack(side=TOP, fill=X)

    def prepare_obj(self):
        self.main_frame = Frame(self.parent, bg="white")
    

    def render(self):
        self.prepare_obj()

        self.main_frame.pack(ipady=10, anchor='w')

        Button(self.main_frame, text="hekll", width=16, pady=0, bd=1, bg="white", fg="black").pack(fill=X)


# buat btn untuk auto search